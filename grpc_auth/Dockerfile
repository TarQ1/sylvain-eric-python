FROM python:3.10-slim-bullseye

RUN mkdir grpc_auth
COPY . grpc_auth/

RUN pip install protobuf grpcio grpcio-tools grpclib

EXPOSE 8001
CMD ["python", "grpc_auth/main.py"]
