Set up a virtual environment for the project:  
`python3 -m venv venv`

Activate the environment:  
`source venv/bin/activate`

Install the dependencies:  
`pip install -r requirements.txt`

Run the database (if needed):  
`make run-db`

Run the API with Uvicorn:  
`uvicorn src.main:app --reload`

Run the database migration:  
`alembic upgrade head` (check if postgresql is up and running. It takes time for the first time)


Hit the POST endpoint and insert the initial data (FOR THE FIRST TIME):  
`curl --request POST --data '{ "type": "bank-draft", "title": "Bank Draft", "position": 0 }' localhost:8000 && curl --request POST --data '{ "type": "bill-of-lading", "title": "Bill of Lading", "position": 1 }' localhost:8000 && curl --request POST --data '{"type": "invoice", "title": "Invoice", "position": 2}' localhost:8000 && curl --request POST --data '{"type": "bank-draft-2", "title": "Bank Draft 2", "position": 3}' localhost:8000 && curl --request POST --data '{"type": "bill-of-lading-2", "title": "Bill of Lading 2", "position": 4}' localhost:8000`
