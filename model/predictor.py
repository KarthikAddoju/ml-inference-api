from model.model import load_model

class Predictor:
    """
    Predictor class responsible for handling model inference.
    """

    def __init__(self):
        self.model = load_model()

    def predict(self, value: float):
        prediction = self.model.predict([[value]])[0]
        probability = self.model.predict_proba([[value]])[0].max()

        return {
            "prediction": int(prediction),
            "confidence": round(float(probability), 3)
        }
