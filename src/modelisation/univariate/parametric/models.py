from lifelines import ExponentialFitter, LogNormalFitter, WeibullFitter

model_type = LogNormalFitter | ExponentialFitter | WeibullFitter


def create_models() -> dict[str, model_type]:
    models = {
        "Weibull": WeibullFitter(),
        "Exponentiel": ExponentialFitter(),
        "Log-normal": LogNormalFitter(),
    }

    return models
