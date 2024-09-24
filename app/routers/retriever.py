
import uuid

from app.chains.retriever import retrieve_chain, requests
from app.schemas import RetrieveRequest, RetrieveResponse, Retrieved

from fastapi import APIRouter, BackgroundTasks, Request, HTTPException

# Creating a router with a prefix for retrieval endpoints
retriever_router = APIRouter(prefix="/retriever")


@retriever_router.post(
    "/",
    summary="Retrieve related texts.",
    responses={
        201: {"description": "Successfully initiated task."},
    },
)
async def retrieve_text(
        r: RetrieveRequest, background_tasks: BackgroundTasks
) -> RetrieveResponse:
    # Generate a unique ID for the request
    req_id = uuid.uuid4()

    # Add the retrieval task to the background tasks
    background_tasks.add_task(
        retrieve_chain,
        req_id,
        r.query
    )

    # Return a response indicating the task initiation
    return RetrieveResponse(id=req_id, completed=False)


@retriever_router.get(
    "/{id}",
    summary="Get retrieved texts.",
    responses={
        200: {"description": "Successfully fetched texts."},
        404: {"description": "query not found."},
    },
)
async def get_texts(r: Request, id: uuid.UUID):
    if id in requests:
        req = requests[id]

        # Return the retrieved texts
        return Retrieved(id=req.id, completed=req.completed, texts=req.texts)

    # Raise an error if the ID is not found
    raise HTTPException(status_code=404, detail="ID not found")
