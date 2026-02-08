from fastapi import APIRouter
from model.predictor import Predictor

router = APIRouter()
predictor = Predictor()

@router.post("/predict")
def predict(value: float):
    """
    API endpoint to perform ML inference.
    """
    return predictor.predict(value)
