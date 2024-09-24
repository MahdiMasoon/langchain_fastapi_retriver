
import uuid

from pydantic import BaseModel, Field


# Model for the retrieval request
class RetrieveRequest(BaseModel):
    query: str = Field(description="Query text")


# Model for the retrieval response
class RetrieveResponse(BaseModel):
    id: uuid.UUID = Field(description="ID Of the retrieved texts")
    completed: bool = Field(
        description="Flag indicating if the retrieving was completed"
    )


# Model for the final retrieved texts
class Retrieved(RetrieveResponse):
    texts: list[str] = Field(description="The retrieved texts")
