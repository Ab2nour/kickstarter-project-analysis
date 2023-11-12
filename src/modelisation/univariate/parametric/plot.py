import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

from src.modelisation.univariate.parametric.models import model_type


def plot_estimation(
    model: model_type,
    model_name: str,
    event_times: pd.Series | np.ndarray,
    event_observed: pd.Series | np.ndarray,
    plot_title: str,
    plot_label: str,
) -> None:
    model.fit(event_times, event_observed)
    model.plot_survival_function(plot_label)

    plt.title(plot_title)


def plot_estimations(
    models: dict[str, model_type],
    event_times: pd.Series | np.ndarray,
    event_observed: pd.Series | np.ndarray,
    same_plot: bool = False,
) -> None:
    for model_name, model in models.items():
        title = "Fonction de survie"
        label = f"Modèle {model_name}"
        plot_estimation(model, model_name, event_times, event_observed, title, label)

        if not same_plot:
            plt.show()
