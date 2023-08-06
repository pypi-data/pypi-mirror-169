from typing import List, Optional, Tuple

import numpy as np
import pandas as pd
from pydantic import BaseModel, ValidationError

from regression_model.config.core import config


def drop_na_inputs(*, input_data: pd.DataFrame) -> pd.DataFrame:
    """
    Check model inputs for na values and filter
    """
    validated_data = input_data.copy()
    new_vars_with_na = [
        var
        for var in config.model_config.features
        if validated_data[var].isnull().sum() > 0
    ]
    validated_data.dropna(subset=new_vars_with_na, inplace=True)

    return validated_data


def validate_inputs(*, input_data: pd.DataFrame) -> Tuple[pd.DataFrame, Optional[dict]]:
    """
    Check model inputs for unprocessable values
    """
    target_ = config.model_config.target
    if target_ in input_data.columns:
        input_data.loc[:, target_] = input_data[target_].apply(np.log)
    relevant_data = input_data[config.model_config.features].copy()
    validated_data = drop_na_inputs(input_data=relevant_data)
    errors = None

    try:
        MultipleHouseDataInputs(
            inputs=validated_data.replace({np.nan: None}).to_dict(orient="records")
        )
    except ValidationError as error:
        errors = error.json()

    return validated_data, errors


class HouseDataInputSchema(BaseModel):
    town: Optional[str]
    flat_type: Optional[str]
    storey_range: Optional[str]
    floor_area_sqm: Optional[float]
    flat_model: Optional[str]
    lease_commence_data: Optional[int]
    remaining_lease: Optional[str]
    dist_school: Optional[float]
    dist_mrt: Optional[float]
    dist_supermarket: Optional[float]
    dist_hawker: Optional[float]
    dist_npc: Optional[float]
    dist_central: Optional[float]
    id: Optional[int]


class MultipleHouseDataInputs(BaseModel):
    inputs: List[HouseDataInputSchema]
