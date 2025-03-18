from lifelines import KaplanMeierFitter, NelsonAalenFitter

survival_model_type = KaplanMeierFitter
hazard_model_type = NelsonAalenFitter


def create_survival_models() -> dict[str, survival_model_type]:
    models = {
        "Kaplan-Meier": KaplanMeierFitter(),
    }

    return models


def create_hazard_models() -> dict[str, hazard_model_type]:
    models = {
        "Nelson-Aalen": NelsonAalenFitter(),
    }

    return models
