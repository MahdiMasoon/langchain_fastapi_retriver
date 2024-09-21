from pydantic import BaseModel, Field
from typing import List
import uuid


class RetrieveRequest(BaseModel):
    query: str = Field(description="Query text")


class RetrieveResponse(BaseModel):
    id: uuid.UUID = Field(description="ID Of the retrieved texts")
    completed: bool = Field(
        description="Flag indicating if the retrieving was completed"
    )


class Retrieved(RetrieveResponse):
    texts: list[str] = Field(description="The retrieved texts")
