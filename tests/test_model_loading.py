# tests/test_model_loading.py

import os
import numpy as np
import pandas as pd
from src.pipeline.predict_pipeline import Predictpipeline


def test_model_file_exists():
    assert os.path.exists("artifacts/model.pkl")


def test_prediction_runs():
    data = pd.DataFrame([{
        "gender": "male",
        "race_ethnicity": "group A",
        "parental_level_of_education": "bachelor's degree",
        "lunch": "standard",
        "test_preparation_course": "none",
        "reading_score": 70,
        "writing_score": 72
    }])

    preds = Predictpipeline().predict(data)

    assert preds is not None
    assert len(preds) == 1
    assert isinstance(preds, (list, tuple, np.ndarray))
