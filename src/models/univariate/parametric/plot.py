from typing import Literal

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

from src.plot.constants import hazard, survival
from src.models.univariate.parametric.models import model_type

estimation_type = Literal["survival", "hazard"]


def plot_estimation(
    plot_type: estimation_type,
    model: model_type,
    event_times: pd.Series | np.ndarray,
    event_observed: pd.Series | np.ndarray,
    plot_label: str,
    show_at_risk_counts: bool = False,
) -> None:
    model.fit(event_times, event_observed)

    if plot_type == "survival":
        model.plot_survival_function(
            label=plot_label, at_risk_counts=show_at_risk_counts
        )

        plt.title(survival["function_title"])
        plt.xlabel(survival["xlabel"])
        plt.ylabel(survival["ylabel"])
    elif plot_type == "hazard":
        model.plot_cumulative_hazard(
            label=plot_label, at_risk_counts=show_at_risk_counts
        )

        plt.title(hazard["function_title"])
        plt.xlabel(hazard["xlabel"])
        plt.ylabel(hazard["ylabel"])


def plot_estimations(
    plot_type: estimation_type,
    models: dict[str, model_type],
    event_times: pd.Series | np.ndarray,
    event_observed: pd.Series | np.ndarray,
    same_plot: bool = False,
    show_at_risk_counts: bool = False,
) -> None:
    for model_name, model in models.items():
        label = f"Modèle {model_name}"
        plot_estimation(
            plot_type,
            model,
            event_times,
            event_observed,
            label,
            show_at_risk_counts,
        )

        if not same_plot:
            plt.show()


def plot_survival_estimation(
    models: dict[str, model_type],
    event_times: pd.Series | np.ndarray,
    event_observed: pd.Series | np.ndarray,
    plot_label: str,
    show_at_risk_counts: bool = False,
) -> None:
    plot_estimation(
        "survival", models, event_times, event_observed, plot_label, show_at_risk_counts
    )


def plot_survival_estimations(
    models: dict[str, model_type],
    event_times: pd.Series | np.ndarray,
    event_observed: pd.Series | np.ndarray,
    same_plot: bool = False,
    show_at_risk_counts: bool = False,
) -> None:
    plot_estimations(
        "survival", models, event_times, event_observed, same_plot, show_at_risk_counts
    )


def plot_hazard_estimation(
    models: dict[str, model_type],
    event_times: pd.Series | np.ndarray,
    event_observed: pd.Series | np.ndarray,
    plot_label: str,
    show_at_risk_counts: bool = False,
) -> None:
    plot_estimation(
        "hazard", models, event_times, event_observed, plot_label, show_at_risk_counts
    )


def plot_hazard_estimations(
    models: dict[str, model_type],
    event_times: pd.Series | np.ndarray,
    event_observed: pd.Series | np.ndarray,
    same_plot: bool = False,
    show_at_risk_counts: bool = False,
) -> None:
    plot_estimations(
        "hazard", models, event_times, event_observed, same_plot, show_at_risk_counts
    )
