import uuid

from fastapi import APIRouter, BackgroundTasks, Request, HTTPException

from app.chains.retriever import retrieve_chain, requests
from app.schemas import RetrieveRequest, RetrieveResponse, Retrieved

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
    req_id = uuid.uuid4()

    background_tasks.add_task(
        retrieve_chain,
        req_id,
        r.query
    )

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
        return Retrieved(id=req.id, completed= req.completed, texts=req.texts)
    raise HTTPException(status_code=404, detail="ID not found")