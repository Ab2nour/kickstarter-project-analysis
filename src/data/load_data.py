import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from src.data.data_dtypes import df_original_dtypes
from src.utils import get_project_root


def get_df() -> pd.DataFrame:
    project_root = get_project_root()
    dfs = [pd.read_csv(f"{project_root}/data/kickstarter_{i}.csv") for i in range(1, 5)]
    df = pd.concat(dfs, ignore_index=True)

    return df
