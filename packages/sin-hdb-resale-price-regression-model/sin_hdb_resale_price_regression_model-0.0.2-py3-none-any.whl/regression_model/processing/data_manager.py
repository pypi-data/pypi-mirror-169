import typing as t
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline

from regression_model import __version__ as _version
from regression_model.config.core import DATASET_DIR, TRAINED_MODEL_DIR, config


def load_dataset(*, file_name: str) -> pd.DataFrame:
    df = pd.read_csv(Path(f"{DATASET_DIR}/{file_name}"))

    target_ = config.model_config.target
    if target_ in df.columns:
        df.loc[:, target_] = df[target_].apply(np.log)

    df.drop(columns=config.model_config.dropped_feature, inplace=True)

    return df


def save_pipeline(*, pipeline_to_persist: Pipeline) -> None:
    """
    Persist the pipeline. Save the versioned model, and overwrites
    any previous saved models. This ensures that when the package is
    published, there is only one trained model that can be called,
    and we know exactly how it was built.
    """

    # Prepare verisoned save file name
    save_file_name = f"{config.app_config.pipeline_save_file}{_version}.pkl"
    save_path = TRAINED_MODEL_DIR / save_file_name

    removed_old_pipelines(files_to_keep=[save_file_name])
    joblib.dump(pipeline_to_persist, save_path)


def load_pipeline(*, file_name: str) -> Pipeline:
    """
    Load a persist pipeline
    """
    file_path = TRAINED_MODEL_DIR / file_name
    trained_model = joblib.load(filename=file_path)

    return trained_model


def removed_old_pipelines(*, files_to_keep: t.List[str]) -> None:
    """
    removed old model pipelines. This is ensure there is a simple
    one-to-one mapping between the package version and model
    version to be imported and used by other applications.
    """

    do_not_delete = files_to_keep + ["__init__.py"]
    for model_file in TRAINED_MODEL_DIR.iterdir():
        if model_file.name not in do_not_delete:
            model_file.unlink()
