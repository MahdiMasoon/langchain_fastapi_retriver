# langchain_fastapi_retriever

## Overview
In this project, I wrote a service using FastAPI that fetches pieces of text related to your query from the database using langchain.

## Getting Started

### Running the Server
To start the server, execute the following command:
```bash
fastapi run app/main.py
```

### Interacting with the Service
This service designed to operate using the poll/query/read method. This approach ensures that user requests are not delayed during heavy project usage.

#### Sending a Query
To send a query, use the following command:
```bash
curl -X POST -H "Content-type: application/json" -d '{"query": "your query"}' http://localhost:8000/retrieve/
```

#### Retrieving a Response
To retrieve a response, use the following command:
```bash
curl -X GET -H "Content-type: application/json" http://localhost:8000/vacation/your_query_id
```

## Notes
- Ensure that the server is running before sending queries or retrieving responses.
- Replace `your_query_id` with the actual query ID received from the initial query request.
