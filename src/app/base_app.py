from fastapi import FastAPI
import uvicorn

from src.app.request_body import RequestBody
from src.model.iris_model import clf, iris

app = FastAPI()

@app.get('/')
def main():
    return {'message': 'Welcome to a ML model deployment'}

@app.post('/predict')
def predict(data: RequestBody):
    test_data = [[
        data.sepal_length,
        data.sepal_width,
        data.petal_width,
        data.petal_length
    ]]

    class_idx = clf.predict(test_data)[0]
    return {'class': iris.target_names[class_idx]}