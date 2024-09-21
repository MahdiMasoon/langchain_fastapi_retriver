import time
import uuid
from typing import List
from app.schemas import Retrieved


requests = {}


def retrieve_chain(
    id: uuid.UUID, query: str
):
    print(f'Hi {id}, your query is {query}!!!')
    requests[id] = Retrieved(id=id, completed=False, texts=[])
    time.sleep(60)
    requests[id] = Retrieved(id=id, completed=True, texts=['some', 'retrieved', 'texts'])
