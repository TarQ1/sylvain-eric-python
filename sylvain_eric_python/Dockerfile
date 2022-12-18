FROM python:3.10-slim-bullseye

RUN mkdir /sylvain_eric_python

RUN pip install fastapi uvicorn SQLAlchemy psycopg2-binary protobuf grpcio grpcio-tools grpclib

COPY auth.proto ./sylvain_eric_python
RUN python -m grpc_tools.protoc -I sylvain_eric_python=./sylvain_eric_python --python_out=. --grpc_python_out=. ./sylvain_eric_python/auth.proto

WORKDIR /sylvain_eric_python

COPY database ./database
COPY models ./models
COPY repositories ./repositories
COPY main.py .

WORKDIR /

EXPOSE 8000
CMD ["uvicorn", "sylvain_eric_python.main:app", "--host", "0.0.0.0", "--port", "8000"]
