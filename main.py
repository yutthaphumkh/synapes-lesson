from fastapi import FastAPI, Path, Body
import uvicorn
from pydantic import BaseModel, Field
import numpy as np
import pandas as pd
import joblib

app = FastAPI(title="Sample FastAPI",
              description="For education", version="1.0")

model = joblib.load('c45_classifier.pkl')

class Input(BaseModel):
    pregnancies : float = Field(0, example=1) 
    glocose: float = Field(0, example=1) 
    blood_pressure: float = Field(0, example=10) 
    skin_thickness: float = Field(0, example=1)
    insulin: float = Field(1)
    diabetes_ped_func: float = Field(0, example=1)
    age: float = Field(..., example=15)
    bmi: float = Field(..., example=33)
    
@app.post("/prediction")
def prediction(data: Input):
    data = dict(data)
    data_arr=np.array([v for (_,v) in data.items()])
    data_rr=data_arr.reshape(1,-1)
    a=model.predict(data_rr)
    result = {"status": "OK", "result":int(a)}
    return result


if __name__ == "__main__":
	uvicorn.run("main:app", port=5001, log_level="info", reload=True, host="0.0.0.0")