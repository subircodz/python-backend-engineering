from dataclasses import dataclass
from enum import Enum


class Status(Enum):
    UP = "up"
    DOWN = "down"
    MAINTENANCE = "maintenance"


@dataclass
class Server:
    name: str
    status: Status


class Monitor:
    def __init__(self):
        self.servers = set()
        self.down_servers = set()

    def add_server(self, server: Server):
        if server.name in self.servers:
            return f"{server.name.upper()} already added for monitoring."

        self.servers.add(server.name)

        if server.status == Status.DOWN:
            return self.mark_down(server)

        return f"{server.name} is added for monitoring."

    def mark_down(self, server: Server):
        if server.name not in self.servers:
            return f"{server.name.upper()} server has not been registered."

        if server.name in self.down_servers:
            return f"{server.name.upper()} server is already marked DOWN."

        server.status = Status.DOWN
        self.down_servers.add(server.name)
        return f"{server.name.upper()} server has been marked DOWN."

    def mark_up(self, server: Server):
        if server.name not in self.servers:
            return f"{server.name.upper()} server has not been registered."

        if server.status == Status.UP:
            return f"{server.name.upper()} server is already marked UP."

        server.status = Status.UP
        self.down_servers.discard(server.name)
        return f"{server.name.upper()} server has been marked UP."

    def get_down_servers(self):
        return self.down_servers.copy()


database = Server("database", Status.UP)
web = Server("web", Status.DOWN)
printer = Server("printer", Status.MAINTENANCE)

monitor = Monitor()
print(monitor.add_server(database))
print(monitor.add_server(web))
print(monitor.add_server(printer))
print(monitor.add_server(web))
print(monitor.mark_down(database))
print(monitor.mark_down(database))
print(monitor.mark_down(web))
print(monitor.mark_up(web))
print(f"Servers Down: {monitor.get_down_servers()}")
