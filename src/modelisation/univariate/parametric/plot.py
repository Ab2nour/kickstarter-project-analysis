import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

from src.constants import (
    survival_function_title,
    survival_function_xlabel,
    survival_function_ylabel,
)
from src.modelisation.univariate.parametric.models import model_type


def plot_estimation(
    model: model_type,
    event_times: pd.Series | np.ndarray,
    event_observed: pd.Series | np.ndarray,
    plot_label: str,
) -> None:
    model.fit(event_times, event_observed)
    model.plot_survival_function(label=plot_label)

    plt.title(survival_function_title)
    plt.xlabel(survival_function_xlabel)
    plt.ylabel(survival_function_ylabel)


def plot_estimations(
    models: dict[str, model_type],
    event_times: pd.Series | np.ndarray,
    event_observed: pd.Series | np.ndarray,
    same_plot: bool = False,
) -> None:
    for model_name, model in models.items():
        label = f"Modèle {model_name}"
        plot_estimation(model, event_times, event_observed, label)

        if not same_plot:
            plt.show()
