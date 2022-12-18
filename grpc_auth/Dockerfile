FROM python:3.10-slim-bullseye

RUN mkdir grpc_auth
WORKDIR grpc_auth

RUN pip install protobuf grpcio grpcio-tools grpclib jwt SQLAlchemy psycopg2-binary passlib

COPY auth.proto .
RUN python -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. auth.proto

COPY main.py .
COPY database.py .

EXPOSE 8001
CMD ["python", "main.py"]
