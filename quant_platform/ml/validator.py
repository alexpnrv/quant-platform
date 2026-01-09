import numpy as np
from sklearn.model_selection import TimeSeriesSplit
from sklearn.metrics import accuracy_score

def walk_forward_validation(model, X, y, splits: int = 5):
    tscv = TimeSeriesSplit(n_splits=splits)
    scores = []
    for train_index, test_index in tscv.split(X):
        X_train, X_test = X.iloc[train_index], X.iloc[test_index]
        y_train, y_test = y.iloc[train_index], y.iloc[test_index]
        model.fit(X_train, y_train)
        pred = model.predict(X_test)
        scores.append(accuracy_score(y_test, pred))
    return np.mean(scores)

def detect_drift(current_returns: np.ndarray, previous_returns: np.ndarray, threshold: float = 0.05) -> bool:
    # Simple drift detection based on mean shift.
    mean_shift = abs(current_returns.mean() - previous_returns.mean())
    return mean_shift > threshold