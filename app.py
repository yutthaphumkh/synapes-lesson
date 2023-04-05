from fastapi import FastAPI, Path, Body
import uvicorn
from pydantic import BaseModel, Field

app = FastAPI(title="Sample FastAPI",
              description="For education", version="1.0")

data = {1: "John", 2: "jane"}

@app.get("/api/people")
def get_peoples():
    return data

@app.get("/api/people/{id}")
def get_one_people(id: int = Path()):
    return data[id]

from pydantic import BaseModel, Field

class People(BaseModel):
    id: int = Field(..., description="first name")
    name: str = Field("None", description="last name")
    
@app.post("/api/people-add")
def add_one_people(data: People):
    print(data)
    return data


if __name__ == "__main__":
	uvicorn.run("app:app", port=5000, log_level="info", reload=True, host="0.0.0.0")