# Listing 18.4: A classification API with FastAPI
"""api.py: run with  uvicorn api:app --port 8000"""
import joblib
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="News topic classifier", version="1.0")
# pipeline saved in Listing 7.7
model = joblib.load("reuters_topic_model.joblib")

class Article(BaseModel):
    text: str = Field(min_length=10, max_length=50_000)

class Prediction(BaseModel):
    topic: str
    margin: float
    needs_review: bool
    model_version: str = "reuters-svm-1.0"

@app.post("/classify", response_model=Prediction)
def classify(article: Article):
    scores = model.decision_function([article.text])[0]
    best = int(scores.argmax())
    return Prediction(
        topic=model.classes_[best],
        margin=round(float(scores[best]), 3),
        needs_review=bool(scores[best] < 0.2),
    )
