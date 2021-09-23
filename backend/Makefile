run-db:
	docker run --name fastapi_postgres -p 5432:5432 -e POSTGRES_PASSWORD=mysuperpassword -e POSTGRES_DB=vector_ai -v ${PWD}/db_data:/var/lib/postgresql/data -d postgres
