from pydantic import BaseModel, Field

class Task(BaseModel):
    id:int
    name: str = Field(..., min_length=1, max_length=50)
    description: str = Field(..., min_length=1)
    done: bool = False
