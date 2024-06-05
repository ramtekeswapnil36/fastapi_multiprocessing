from pydantic import BaseModel, Field
from typing import List

class AdditionRequest(BaseModel):
    batchid: str
    payload: List[List[int]] = Field(..., example=[[1, 2], [3, 4]])
