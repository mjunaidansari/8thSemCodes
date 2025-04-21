import Pyro5.api

uri = input("Enter the URI of the remote object: ")
remote_greeting = Pyro5.api.Proxy(uri)

name = input("Enter your name: ")
greeting = remote_greeting.greet(name)
print("Greeting from remote method:", greeting)
# This code defines a Pyro5 client that connects to a remote server and calls the `greet` method of the `Greeting` class.
