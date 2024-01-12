import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
# Import necessary Anvil modules
import anvil.server
import anvil.users
from anvil import HTTPResponse

# Define a server function that can be called from the client-side
@anvil.server.callable
def get_server_message():
    return "Hello from the server!"

# Define a server function to perform some server-side logic
@anvil.server.callable
def perform_server_logic(param):
    # Add your server-side logic here
    result = f"Server logic performed with parameter: {param}"
    return result

# Example of a server function that makes an HTTP request
@anvil.server.callable
def make_http_request():
    # You can use the anvil.http module for making HTTP requests
    response = anvil.http.request("https://api.example.com/data", json={"key": "value"}, method="POST")
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"HTTP Request failed with status code {response.status_code}")

# Example of a server function that requires authentication
@anvil.server.callable(require_user=True)
def restricted_function():
    # This function can only be called by authenticated users
    user = anvil.users.get_user()
    return f"Welcome, {user['email']}!"

# Add more server functions as needed for your application
