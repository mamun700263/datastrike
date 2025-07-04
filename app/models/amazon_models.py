from typing import List
from pydantic import BaseModel, Field

class AmazonSearchResult(BaseModel):
    name:str
    url:url 
    image_url : url
    rating:float
    rated_by : int
