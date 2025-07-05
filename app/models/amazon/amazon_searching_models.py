from typing import List, Optional
from pydantic import BaseModel, Field, HttpUrl


class AmazonSearchResult(BaseModel):
    id: int
    name: str
    url: HttpUrl
    image_url: HttpUrl
    description: Optional[str] = None
    rating: Optional[float] = Field(None, ge=0, le=5)
    rated_by: Optional[int] = Field(0, ge=0)

    class Config:
        orm_mode = True
