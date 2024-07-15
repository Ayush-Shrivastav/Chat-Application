# gRPC Email-Based Authentication

This project demonstrates how to implement email-based authentication using gRPC with Python. The application allows users to register with a unique email, log in to receive a JWT token, and access protected methods using the token.

## Table of Contents
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [Run the Server](#run-the-server)
  - [Run the Client](#run-the-client)
- [Testing with BloomRPC](#testing-with-bloomrpc)
- [Debugging](#debugging)
- [Logging](#logging)

## Requirements

- Python 3.7+
- gRPC
- grpcio-tools
- sqlite3
- jwt

## Installation

1. Clone the Repo and cd to authentication service
2. Create a virtual environment and activate it:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3. Create and edit the .env file and fill the required values:
    ```bash
   cp .env.example .env
    ```
4. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Generate the gRPC code from the protobuf file:
    ```bash
    python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. Authentication.proto
    ```

## Usage

### Run the Server

To start the gRPC server, run the following command:

```bash
python server.py
```

### Run the Client

To interact with the gRPC server using the client, run the following command:

```bash
python client.py
```
## Testing with BloomRPC

BloomRPC is a GUI client for gRPC services, which you can use to test the endpoints.

1. Install BloomRPC:
    Download and install BloomRPC from the official GitHub page.

2. Load the Proto File:
    Open BloomRPC and load the Authentication.proto file.

3. Test Registration:
    Select the Register method from AuthService.
    Fill in the required fields (email, username, password) and click "Invoke".

4. Test Login:
    Select the Login method from AuthService.
    Fill in the required fields (email, password) and click "Invoke".
    Note the JWT token returned in the response.

5. Test AccessProtectedResource:
    Select the AccessProtectedResource method from AuthService.
    Add the JWT token to the metadata with the key authorization.
    Click "Invoke" to access the protected resource.

## Debugging

### Common Issues and Solutions

1. Database Errors:
    Ensure the users.db file is created and writable.
    Verify the sqlite3 installation and connection.

2. JWT Errors:
    Ensure the JWT secret key (JWT_SECRET) is correctly set and consistent between the server and client.
    Check for token expiration and handle it appropriately.

3. gRPC Connection Issues:
    Verify the server is running on the correct port.
    Ensure the client is connecting to the correct server address.

## Logging

Logs are written to the logs folder, with separate log files for the server (server.log) and client (client.log). You can find these log files in the logs directory created by the application. They contain detailed information about requests and responses for debugging purposes.