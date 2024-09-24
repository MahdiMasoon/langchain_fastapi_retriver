
import sys
import uuid
import logging

from app.schemas import Retrieved

from langchain_community.retrievers import TFIDFRetriever

# Configure logging to output to stdout
logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))

# Dictionary to store request states
requests = {}

# Load the retriever
retriever = TFIDFRetriever.load_local("retriever.pkl", allow_dangerous_deserialization=True)


def retrieve_chain(
        id: uuid.UUID, query: str
):
    logging.info(f'Hi {id}, your query is {query}!!!')

    # Initialize request state
    requests[id] = Retrieved(id=id, completed=False, texts=[])

    # Retrieve documents based on the query
    result = retriever.invoke(query)

    logging.debug(f'Hey {id}, your response is ready!!!')

    # Update request state with results
    requests[id] = Retrieved(id=id, completed=True, texts=[res.page_content for res in result])
