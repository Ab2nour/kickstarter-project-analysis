from lifelines import ExponentialFitter, LogNormalFitter, WeibullFitter, GeneralizedGammaFitter

model_type = LogNormalFitter | ExponentialFitter | WeibullFitter | GeneralizedGammaFitter


def create_models() -> dict[str, model_type]:
    models = {
        "Weibull": WeibullFitter(),
        "Exponentiel": ExponentialFitter(),
        "Log-normal": LogNormalFitter(),
        "Gamma-généralisée": GeneralizedGammaFitter(),
    }

    return models
