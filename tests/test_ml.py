import pandas as pd
import numpy as np
from quant_platform.ml.features import create_lag_features
from quant_platform.ml.trainer import ModelTrainer
from quant_platform.ml.validator import walk_forward_validation, detect_drift

def test_lag_features():
    df = pd.DataFrame({"price": [1, 2, 3, 4]})
    df = create_lag_features(df, ["price"], lags=2)
    assert "price_lag1" in df.columns
    assert "price_lag2" in df.columns

def test_trainer_save_load(tmp_path):
    trainer = ModelTrainer()
    X = pd.DataFrame({"a": [1,2,3]})
    y = [0, 1, 0]
    trainer.train(X, y)
    trainer.save(str(tmp_path / "model"))
    trainer.load(str(tmp_path / "model"))
    assert trainer.model is not None

def test_validator():
    X = pd.DataFrame({"a": [1, 2, 3, 4, 5, 6]})
    y = [0, 1, 0, 1, 0, 1]
    trainer = ModelTrainer()
    score = walk_forward_validation(trainer.model, X, pd.Series(y), splits=2)
    assert 0.0 <= score <= 1.0
    assert not detect_drift(np.array([1, 2, 3]), np.array([1, 2, 3]), threshold=0.5)
    assert detect_drift(np.array([1, 2, 3]), np.array([10, 11, 12]), threshold=0.5)