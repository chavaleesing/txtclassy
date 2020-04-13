from main import app
from service.classifier import classify
from pydantic import BaseModel


class Context(BaseModel):
    sentence: str = None


@app.post("/text/classification")
def text_classification(data: Context):
    result = classify(data.sentence)
    return {"class": result}
