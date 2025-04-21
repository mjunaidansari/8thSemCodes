import Pyro5.api

@Pyro5.api.expose
class Greeting:
    def greet(self, name):
        return f"Hello, {name}!"

def main():
    daemon = Pyro5.api.Daemon()                 # Start Pyro5 server
    uri = daemon.register(Greeting)              # Register the Greeting class
    print("Ready. Object URI =", uri)
    daemon.requestLoop()                        # Wait for calls

if __name__ == "__main__":
    main()
# This code defines a Pyro5 server that exposes a `Greeting` class with a `greet` method.
