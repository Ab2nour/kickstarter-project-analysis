import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from models import model_type


def plot_estimations(
    models: dict[str, model_type],
    event_times: pd.Series | np.ndarray,
    event_observed: pd.Series | np.ndarray,
) -> None:
    for model_name, model in models.items():
        model.fit(event_times, event_observed)

        model.plot()
        model.plot_survival_function(label="Fonction de survie")

        plt.title(f"Modèle {model_name}")
        plt.show()
