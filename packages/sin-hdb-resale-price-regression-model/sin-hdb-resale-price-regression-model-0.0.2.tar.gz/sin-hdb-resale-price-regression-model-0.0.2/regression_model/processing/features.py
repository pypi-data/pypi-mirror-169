import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin


class ExtractNumericalValue(BaseEstimator, TransformerMixin):
    """
    Extract the number of years and months of the variable(remaining_lease)
    """

    def __init__(self, variable: str):
        super().__init__()

        self.variable = variable

    def fit(self, X: pd.DataFrame, y: pd.Series = None):
        # We need this step to fit the sklearn pipeline
        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        X = X.copy()
        X.loc[:, self.variable] = X[self.variable].apply(get_remaining_lease)
        return X


class CombineTowns(BaseEstimator, TransformerMixin):
    """
    Categorize the values of the variable(towns)
    """

    def __init__(self, variable: str, mappings: dict):
        super().__init__()

        self.variable = variable
        self.mappings = mappings

    def fit(self, X: pd.DataFrame, y: pd.Series = None):
        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        X = X.copy()
        X.loc[:, self.variable] = X[self.variable].map(self.mappings)
        return X


def get_remaining_lease(x) -> float:

    x = x.split()

    if len(x) == 2:
        return float(x[0])

    return round(float(x[0]) + float(x[2]) / 12, 3)
