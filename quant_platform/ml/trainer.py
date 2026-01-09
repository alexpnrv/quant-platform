import pickle
from pathlib import Path
from sklearn.ensemble import RandomForestClassifier

MODEL_DIR = Path("models")
MODEL_DIR.mkdir(exist_ok=True)

class ModelTrainer:
    """
    Handles model training and persistance.
    """
    def __init__(self, model=None):
        self.model = model or RandomForestClassifier(n_estimators=100, random_state=42)

    def train(self, X, y):
        self.model.fit(X, y)

    def save(self, name: str):
        with open(MODEL_DIR / f"{name}.pkl", "wb") as f:
            pickle.dump(self.model, f) # type: ignore

    def load(self, name: str):
        with open(MODEL_DIR / f"{name}.pkl", "rb") as f:
            self.model = pickle.load(f)