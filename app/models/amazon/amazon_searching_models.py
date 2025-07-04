from typing import List
from pydantic import BaseModel, Field

class AmazonSearchResult(BaseModel):
    id: int
    name:str = Field(..., min_length=3)
    url:url 
    image_url : url
    description: str = Field(..., min_length=1)
    rating:float
    rated_by : int
