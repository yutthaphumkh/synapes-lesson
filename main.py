from fastapi import FastAPI, Path, Body
import uvicorn
from pydantic import BaseModel, Field

app = FastAPI(title="Sample FastAPI",
              description="For education", version="1.0")

class Input(BaseModel):
    pregnancies : float = Field(0) 
    glocose: float = Field(0) 
    blood_pressure: float = Field(0) 
    skin_thickness: float = Field(0)
    insulin: float = Field(0)
    diabetes_ped_func: float = Field(0)
    age: float = Field(0)
    BMI: float = Field(0)
    
@app.post("/prediction")
def prediction(data: Input):
    data = dict(data)
    print(data)
    return data


if __name__ == "__main__":
	uvicorn.run("main:app", port=5001, log_level="info", reload=True, host="0.0.0.0")