from dataclasses import dataclass
from enum import Enum
from actelink.logger import log
from .utils import get_compute_params, PoolFactory
from os import getenv

# makes our enums also inherits from str so that it is JSON serializable
class Calcul(str, Enum):
    """
    Enumération des différents types de calcul
    """
    PrimePureDirecte    = 'PRIME_PURE_DIRECTE'
    """ Calcul de la prime pure directe """
    CoutMoyenFrequence  = 'avg_cost'
    """ Calcul du coût moyen * fréquence """

class Regime(str, Enum):
    """
    Enumération des régimes de sécurité sociale
    """
    General         = 'GENERAL'
    """ Régime général """
    AlsaceMoselle   = 'ALSACE_MOSELLE'
    """ Régime Alsace Moselle """

class NiveauProduit(str, Enum):
    """
    Enumération des différents niveaux de produit
    """
    Bas     = 'BAS'
    """ Niveau de produit bas de gamme """
    Milieu  = 'MILIEU'
    """ Niveau de produit milieu de gamme """
    Haut    = 'HAUT'
    """ Niveau de produit haut de gamme """

class StructureTarifaire(str, Enum):
    """
    Enumération des différents éléments de la structure tarifaire
    """
    PrimePure_AgeMoyen           = 'pp_age_moyen'
    PrimePure_Cas1_Isole         = 'pp_cas1_isole'
    PrimePure_Cas1_2Tetes        = 'pp_cas1_2tetes'
    PrimePure_Cas1_Famille       = 'pp_cas1_famille'
    PrimePure_Cas2_Isole         = 'pp_cas2_isole'
    PrimePure_Cas2_Famille       = 'pp_cas2_famille'
    PrimePure_Cas3_Adulte        = 'pp_cas3_adulte'
    PrimePure_Cas3_Enfant        = 'pp_cas3_enfant'
    PrimePure_Cas4_Unique        = 'pp_cas4_unique'
    PrimePure_Cas5_AdulteEnfant  = 'pp_cas5_adulte_enfant' 
    PrimePure_Cas5_Conjoint      = 'pp_cas5_conjoint'    

    @classmethod
    def is_valid(cls, tarif):
        if isinstance(tarif, cls):
            tarif=tarif.value
        if not tarif in cls.__members__.values():
            return False
        else:
            return True

@dataclass
class TarifDict(dict):
    def __setitem__(self, k, v):
        if not StructureTarifaire.is_valid(k):
            raise KeyError(f"StructureTarifaire {k} is not valid")
        else:
            super().__setitem__(StructureTarifaire(k), v)

@dataclass
class Context(object):
    """
    Object représentant un contexte de calcul
    """
    millesime:  str
    """ Millésime """
    offre:      str
    """ Offre """
    guarantyId: str
    """ Identifiant unique de garantie """
    calcul:     Calcul
    """ Type de calcul """

    @classmethod
    def from_dict(cls, context: dict):
        return cls(**context)

    @classmethod
    def from_string(cls, context: str):
        new_ctx = {}
        ctx_values = context.split(".")
        for idx, field in enumerate(Context.__dataclass_fields__.keys()):
            if idx >= len(ctx_values):
                return None
            new_ctx[field] = ctx_values[idx]
        return cls(**new_ctx)

    # implements __hash__ so that Context is hashable hence can be used as a key
    def __hash__(self):
        return hash((self.millesime, self.offre, self.guarantyId, self.calcul))

__functions = {}
__replace_br = getenv("REPLACE_BR_WITH_BRSS", "false") == "true"

def add(fname: str, fcallback: object, context: Context) -> None:
    log.info(f"{fname}, {fcallback}, {context})")
    __functions[context] = {"functionName": fname, "callback": fcallback}

def get() -> list:
    return [{"context": key, "functionName": value["functionName"]} for key,value in __functions.items()]

def __compute_wrapper(func, ctx, params, result):
    return func(ctx, params, result)

def compute(contexts: dict) -> list:
    #TODO measure processing time in DEBUG mode only
    import time
    start = time.perf_counter()

    count = 0
    guarantees = []
    computation_func = None

    for compute_task in contexts["computationContexts"]["contexts"]:
        context = Context.from_dict(compute_task["context"])
        computation_func = __functions.get(context)
        if computation_func is not None:
            log.info(f": prepare computation task for {context.guarantyId}")
            result = {
                "context": compute_task["context"], 
                "function_name": computation_func["functionName"],
                "rate": TarifDict.fromkeys(tuple(StructureTarifaire.__members__.values()))}
            # dunno why parameters is an array..
            compute_params = get_compute_params(compute_task["parameters"][0], contexts["computationContexts"], __replace_br)
            guarantees.append((computation_func["callback"], context, compute_params, result))
            count += 1
        else:
            log.error(f"lack declaration {context}")

    results = {}
    results["results"] = PoolFactory.get_instance().starmap(__compute_wrapper, guarantees)

    end = time.perf_counter()
    log.info(f"EXECUTION TIME ({count} guarantees): {end-start}")

    return results
