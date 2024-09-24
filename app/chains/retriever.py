import logging
import sys
import uuid

from langchain_community.retrievers import TFIDFRetriever

from app.schemas import Retrieved

logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))

requests = {}

retriever = TFIDFRetriever.load_local("retriever.pkl", allow_dangerous_deserialization=True)


def retrieve_chain(
        id: uuid.UUID, query: str
):
    logging.info(f'Hi {id}, your query is {query}!!!')
    requests[id] = Retrieved(id=id, completed=False, texts=[])
    result = retriever.invoke(query)
    logging.debug(f'Hey {id}, your response is ready!!!')
    requests[id] = Retrieved(id=id, completed=True, texts=[res.page_content for res in result])
