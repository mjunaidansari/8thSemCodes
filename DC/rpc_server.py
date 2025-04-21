from xmlrpc.server import SimpleXMLRPCServer

# Create the server
server = SimpleXMLRPCServer(("127.0.0.1", 8000))
print("RPC Server is running on port 8000...")

# Define a remote function
def say_hello(name):
    return f"Hello, {name}! Welcome to Python RPC."

# Register the function to make it remotely accessible
server.register_function(say_hello, "say_hello")

# Run the server indefinitely
server.serve_forever()
