import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

from src.modelisation.univariate.parametric.models import model_type


def plot_estimations(
    models: dict[str, model_type],
    event_times: pd.Series | np.ndarray,
    event_observed: pd.Series | np.ndarray,
    same_plot: bool = False,
) -> None:
    for model_name, model in models.items():
        model.fit(event_times, event_observed)

        model.plot_survival_function(label=f"Modèle {model_name}")

        plt.title("Fonction de survie")

        if not same_plot:
            plt.show()
