from lifelines import (
    ExponentialFitter,
    GeneralizedGammaFitter,
    LogLogisticFitter,
    LogNormalFitter,
    PiecewiseExponentialFitter,
    WeibullFitter,
)

model_type = (
    LogNormalFitter
    | LogLogisticFitter
    | ExponentialFitter
    | WeibullFitter
    | GeneralizedGammaFitter
    | PiecewiseExponentialFitter
)


def create_models() -> dict[str, model_type]:
    """Create the univariate parametric models."""
    models = {
        "Weibull": WeibullFitter(),
        "Exponentiel": ExponentialFitter(),
        "Log-normal": LogNormalFitter(),
        "Log-logistique": LogLogisticFitter(),
        "Gamma-généralisée": GeneralizedGammaFitter(),
        "Exponentiel par morceau": PiecewiseExponentialFitter([9, 21, 29]),
    }

    return models
