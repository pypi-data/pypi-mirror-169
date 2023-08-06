from feature_engine.encoding import OneHotEncoder, OrdinalEncoder, RareLabelEncoder
from feature_engine.outliers import Winsorizer
from feature_engine.transformation import YeoJohnsonTransformer
from sklearn.pipeline import Pipeline
from xgboost import XGBRegressor

from regression_model.config.core import config
from regression_model.processing import features as pp

housing_price_pipe = Pipeline(
    [
        # ====== PREPROCESSING ======
        # extract the number of years and months from the
        # variable ('remaining_lease')
        (
            "extract_numerical_values",
            pp.ExtractNumericalValue(variable=config.model_config.remaining_lease),
        ),
        # categorize the values of the variable ('towns')
        (
            "group_towns",
            pp.CombineTowns(
                variable=config.model_config.town,
                mappings=config.model_config.town_mappings,
            ),
        ),
        # ====== Numerical Encoding ======
        # remove outliers
        (
            "remove_outliers",
            Winsorizer(
                capping_method="iqr",
                tail="both",
                fold=1.5,
                variables=config.model_config.with_outliers,
            ),
        ),
        # perform Yeo-Johnson transformation on skewed features
        (
            "yeo_johnson_transformation",
            YeoJohnsonTransformer(variables=config.model_config.skewed_features),
        ),
        # ====== Categorical Encoding ======
        # rare labels encoding
        (
            "rare_label_encoding",
            RareLabelEncoder(
                n_categories=5, variables=config.model_config.with_rarelabels
            ),
        ),
        # one hot encoding
        (
            "one_hot_encoding",
            OneHotEncoder(variables=config.model_config.by_onehot, drop_last=True),
        ),
        # ordinal encoding
        ("ordinal_encoding", OrdinalEncoder(variables=config.model_config.by_ordinal)),
        # ====== Apply Model ======
        (
            "xgboost_regressor",
            XGBRegressor(random_state=config.model_config.random_state),
        ),
    ]
)
