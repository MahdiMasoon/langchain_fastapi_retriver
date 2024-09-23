import time
import uuid
import sys
from app.schemas import Retrieved
import logging

logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))

requests = {}


def retrieve_chain(
    id: uuid.UUID, query: str
):
    logging.info(f'Hi {id}, your query is {query}!!!')
    requests[id] = Retrieved(id=id, completed=False, texts=[])
    time.sleep(20)
    logging.debug(f'Hey {id}, your response is ready!!!')
    requests[id] = Retrieved(id=id, completed=True, texts=['some', 'retrieved', 'texts'])
