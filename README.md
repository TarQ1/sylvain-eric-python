# Pokémon Card API

MTI 2023 Python project

eric.cloyd

sylvain.ecuer

## Install

```sh
poetry install
```

## Execute

```sh
# start database
docker-compose up py_db
# start app
poetry run start
```

The API is available on port 80.

Online documentation is available at `/docs` while the server is running.

## Run Tests

```sh
# start database
docker-compose up py_db
# run tests
poetry run pytest
```

## Docker Version

```sh
# start all services (app, auth, db)
docker-compose up
```

The API is available on port 8000.

Online documentation is available at `/docs` while the server is running.
