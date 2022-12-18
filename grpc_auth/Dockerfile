FROM python:3.10-slim-bullseye

RUN mkdir grpc_auth
WORKDIR grpc_auth

COPY . .

RUN pip install protobuf grpcio grpcio-tools grpclib

RUN mkdir dist
RUN python -m grpc_tools.protoc --proto_path=./ --python_out=dist --grpc_python_out=./dist auth.proto

EXPOSE 8001
CMD ["python", "main.py"]
