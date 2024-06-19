# artpy (Abandoned)

Aligned Rank Transform for Nonparametric Factorial ANOVAs for python.

This project is unfortunately abandoned.
If you found this repo through search and have found no other solution, here is hoping that the below piece of RPY code may be of help.

```python3
import numpy as np
import pandas as pd
from scipy.stats import mannwhitneyu
from rpy2 import robjects as robj
from rpy2.robjects.packages import importr
from rpy2.robjects import pandas2ri
artool = importr("ARTool")
pandas2ri.activate()

def art_2by2(df: pd.DataFrame, feature: str, group: str):
    feature_wide = df[["Unnamed: 0", feature, "all", "group"]]
    feature_long = feature_wide.melt(id_vars=["Unnamed: 0", "group"], value_vars=[feature, "all"])
    feature_long = feature_long.query(f"group in ('wt', '{group}')")
    feature_long.loc[feature_long["value"] < 0, "value"] = 0
    feature_long["group"] = feature_long["group"].astype("category")
    feature_long["variable"] = feature_long["variable"].astype("category")
    r_df = pandas2ri.py2rpy(feature_long)
    model = artool.art(robj.Formula("value ~ group * variable"), data=r_df)
    anova = robj.r["anova"]
    return anova(model)
```
