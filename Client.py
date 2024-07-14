import grpc
import logging
import os
import Authentication_pb2, Authentication_pb2_grpc

log_folder = 'logs'
os.makedirs(log_folder, exist_ok=True)
logging.basicConfig(level=logging.INFO, filename=os.path.join(log_folder, 'client.log'), filemode='a',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = Authentication_pb2_grpc.AuthServiceStub(channel)

        # Try to register a new user
        try:
            logger.info("Sending Register request.")
            response = stub.Register(Authentication_pb2.RegisterRequest(email='test@example.com', username='testuser', password='testpassword'))
            logger.info("Register response: %s", response.message)
            print(response.message)
        except grpc.RpcError as e:
            logger.info("Registration Error: %s", e)
            if e.code() == grpc.StatusCode.ALREADY_EXISTS:
                print(f"Error: {e.details()}")
            else:
                print(f"Unexpected error: {e}")

        # Log in with the registered user
        try:
            logger.info("Sending Login request.")           
            response = stub.Login(Authentication_pb2.LoginRequest(email='test@example.com', password='testpassword'))
            token = response.token
            logger.info("Login response: %s", token)
            print(f'Token: {token}')
        except grpc.RpcError as e:
            logger.info("Login Error: %s", e)
            print(f"Login error: {e.details()}")

        # Access a protected resource
        try:
            logger.info("Sending AccessProtectedResource  request.")
            metadata = [('authorization', token)]
            response = stub.AccessProtectedResource(Authentication_pb2.Empty(), metadata=metadata)
            logger.info("AccessProtectedResource response: %s", response.message)
            print(response.message)
        except grpc.RpcError as e:
            logger.info("Access Error: %s", e)
            print(f"Access error: {e.details()}")

        # Clean up the database after tests
        try:
            stub.CleanupDb(Authentication_pb2.Empty())
            print("Database cleaned up.")
        except grpc.RpcError as e:
            print(f"Cleanup error: {e.details()}")

if __name__ == '__main__':
    run()
