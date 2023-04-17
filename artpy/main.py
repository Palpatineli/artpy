from typing import List, Dict, Tuple
import numpy as np
import pandas as pd

def art(factors: List[str], value: str, data: pd.DataFrame) -> Tuple[pd.DataFrame, Dict[str, List[Dict[str, float]]]]:
    unincluded_factor = np.setdiff1d(factors, data.columns)
    if len(factors) > 3 or len(factors) < 2:
        raise ValueError("Only works for dimensions 2 and 3!")
    if unincluded_factor.size > 0:
        raise ValueError("factor {} not found in data!".format(', '.join(unincluded_factor)))
    if np.isin(value, data.columns) and not np.isin(value, factors):
        raise ValueError(f"invalid value name {value}")
    # convert the cell mean to high dimensional array
    ndim = len(factors)
    factor_lists = [np.sort(np.unique(data[x])) for x in factors]
    cell_means = np.empty([len(x) for x in factor_lists], dtype=float)
    def walk(state, )
    return anova, contrasts
