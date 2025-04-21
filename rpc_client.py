import xmlrpc.client

# Use /RPC2 instead of /
server = xmlrpc.client.ServerProxy("http://127.0.0.1:8000/RPC2")

name = input("Enter your name: ")
response = server.say_hello(name)
print("Server Response:", response)
