from multiprocessing import Pool

class PoolFactory:
    __pool = None
    @staticmethod
    def get_instance() -> Pool:
        if PoolFactory.__pool is None :
            PoolFactory.__pool = Pool()
        return PoolFactory.__pool

def get_compute_params(guaranty_params: dict, level_params: dict, replace_br: bool) -> dict:
    compute_params = {} | {"parameters": guaranty_params}
    # we dont have to copy the whole demography, we can simply point to it:
    compute_params["demography"]        = level_params["demography"]
    compute_params["levelOfProduct"]    = level_params["levelOfProduct"]
    compute_params["regime"]            = level_params["regime"]
    if replace_br is True and compute_params["parameters"]["bases"][0]["guaranteeValue"]["unit"] == "% BR":
        compute_params["parameters"]["bases"][0]["guaranteeValue"]["unit"] = "% BRSS"
    return compute_params
