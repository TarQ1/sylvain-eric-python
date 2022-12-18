from concurrent import futures

import auth_pb2
import auth_pb2_grpc
import grpc
import jwt
from database import SessionLocal  # type: ignore
from passlib.context import CryptContext
from sqlalchemy import Column, Integer, String  # type: ignore
from sqlalchemy.ext.declarative import declarative_base  # type: ignore

db = SessionLocal()


class UserDbo(declarative_base()):  # type: ignore
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)


class AuthService(auth_pb2_grpc.AuthServiceServicer):
    def Register(self, request, context):
        pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        hash = pwd_context.hash(request.password)

        try:
            dbo = UserDbo(username=request.username, password=hash)
            db.add(dbo)
            db.commit()
        except Exception as e:
            return auth_pb2.RegisterResponse(error=str(e))

        return auth_pb2.RegisterResponse(user=request.username, error="OK")

    def Login(self, request, context):
        db_user: UserDbo = db.query(UserDbo).filter_by(
            username=request.username).first()

        pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        is_correct = pwd_context.verify(request.password, db_user.password)

        if is_correct:
            jwt_payload = {"sub": db_user.username}
            jwt_token = jwt.encode(jwt_payload, "secret", algorithm="HS256")

            return auth_pb2.LoginResponse(user=db_user.username, jwt=jwt_token, error="OK")

        return auth_pb2.LoginResponse(error="Wrong username/password combination")


port = '8001'
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
auth_pb2_grpc.add_AuthServiceServicer_to_server(AuthService(), server)
server.add_insecure_port('[::]:' + port)
server.start()
print("Server started, listening on " + port)
server.wait_for_termination()
db.close()
