from lifelines import (
    ExponentialFitter,
    GeneralizedGammaFitter,
    LogNormalFitter,
    WeibullFitter,
)

model_type = (
    LogNormalFitter | ExponentialFitter | WeibullFitter | GeneralizedGammaFitter
)


def create_models() -> dict[str, model_type]:
    """Create the univariate parametric models."""
    models = {
        "Weibull": WeibullFitter(),
        "Exponentiel": ExponentialFitter(),
        "Log-normal": LogNormalFitter(),
        "Gamma-généralisée": GeneralizedGammaFitter(),
    }

    return models
