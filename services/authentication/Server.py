import grpc
from concurrent import futures
import jwt
import time
import sqlite3
import threading
import logging
import Authentication_pb2, Authentication_pb2_grpc
import os
from dotenv import load_dotenv

load_dotenv()

# Retrieve the secret key from the environment variable
jwt_secret_key = os.getenv('JWT_SECRET_KEY')

# Check if the key is None and raise an error if it is not set
if not jwt_secret_key:
    raise ValueError("No JWT_SECRET_KEY set for Flask application")

# Thread-local storage for database connections
thread_local = threading.local()

def get_db_connection():
    if not hasattr(thread_local, 'conn'):
        thread_local.conn = sqlite3.connect('users.db', check_same_thread=False)
        thread_local.cursor = thread_local.conn.cursor()
        thread_local.cursor.execute('''CREATE TABLE IF NOT EXISTS users
                                      (id INTEGER PRIMARY KEY, email TEXT UNIQUE, username TEXT, password TEXT)''')
        thread_local.conn.commit()
    return thread_local.conn, thread_local.cursor

def cleanup_db():
    conn, cursor = get_db_connection()
    cursor.execute('DELETE FROM users')
    conn.commit()

log_folder = 'logs'
os.makedirs(log_folder, exist_ok=True)
logging.basicConfig(level=logging.INFO, filename=os.path.join(log_folder, 'server.log'), filemode='a',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class AuthServiceServicer(Authentication_pb2_grpc.AuthServiceServicer):

    def Register(self, request, context):
        logger.info("Register request received: %s", request.email)
        conn, cursor = get_db_connection()
        try:
            cursor.execute('INSERT INTO users (email, username, password) VALUES (?, ?, ?)',
                           (request.email, request.username, request.password))
            conn.commit()
            return Authentication_pb2.RegisterResponse(message="User registered successfully.")
        except sqlite3.IntegrityError:
            context.set_code(grpc.StatusCode.ALREADY_EXISTS)
            context.set_details("Email already exists.")
            return Authentication_pb2.RegisterResponse(message="Email already exists.")
    
    def Login(self, request, context):
        logger.info("Login request received: %s", request.email)
        conn, cursor = get_db_connection()
        cursor.execute('SELECT * FROM users WHERE email=? AND password=?', (request.email, request.password))
        user = cursor.fetchone()
        if user:
            token = jwt.encode({'email': request.email, 'exp': time.time() + 600}, jwt_secret_key, algorithm='HS256')
            return Authentication_pb2.LoginResponse(token=token)
        else:
            context.set_code(grpc.StatusCode.UNAUTHENTICATED)
            context.set_details("Invalid email or password.")
            return Authentication_pb2.LoginResponse(token="")

    def AccessProtectedResource(self, request, context):
        token = dict(context.invocation_metadata()).get('authorization')
        logger.info("AccessProtectedResource request received with metadata: %s", context.invocation_metadata())
        if token is None:
            context.set_code(grpc.StatusCode.UNAUTHENTICATED)
            context.set_details("Token is missing.")
            return Authentication_pb2.AccessProtectedResourceResponse(message="Unauthorized")

        try:
            jwt.decode(token, jwt_secret_key, algorithms=['HS256'])
            return Authentication_pb2.AccessProtectedResourceResponse(message="Access granted to protected method.")
        except jwt.ExpiredSignatureError:
            context.set_code(grpc.StatusCode.UNAUTHENTICATED)
            context.set_details("Token has expired.")
            return Authentication_pb2.AccessProtectedResourceResponse(message="Unauthorized")
        except jwt.InvalidTokenError:
            context.set_code(grpc.StatusCode.UNAUTHENTICATED)
            context.set_details("Invalid token.")
            return Authentication_pb2.AccessProtectedResourceResponse(message="Unauthorized")

    def CleanupDb(self, request, context):
        cleanup_db()
        return Authentication_pb2.Empty()

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    Authentication_pb2_grpc.add_AuthServiceServicer_to_server(AuthServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started and listening on port 50051. Waiting for termination...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
