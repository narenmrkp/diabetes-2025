from fastapi import FastAPI
import pickle
import pandas as pd

app = FastAPI(title="Diabetes Prediction API")

# Load trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.get("/")
def read_root():
    return {"message": "Welcome to Diabetes Prediction API"}

@app.post("/predict/")
def predict(data: dict):
    df = pd.DataFrame([data])
    prediction = model.predict(df)
    return {"predicted_progression": float(prediction[0])}
