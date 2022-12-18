from concurrent import futures

import auth_pb2
import auth_pb2_grpc
import grpc
import jwt


class AuthService(auth_pb2_grpc.AuthServiceServicer):
    def login(self, request, context):
        # Validate the username and password
        if request.username != "test" or request.password != "password":
            raise ValueError("Invalid username or password")

        # Generate a JWT
        jwt_payload = {"sub": request.username}
        jwt_token = jwt.encode(jwt_payload, "secret", algorithm="HS256")

        # Return the JWT
        return auth_pb2.LoginResponse(jwt=jwt_token)


port = '8001'
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
auth_pb2_grpc.add_AuthServiceServicer_to_server(AuthService(), server)
server.add_insecure_port('[::]:' + port)
server.start()
print("Server started, listening on " + port)
server.wait_for_termination()
