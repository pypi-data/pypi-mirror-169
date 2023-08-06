from enum import IntEnum, unique

import zmq
from zmq import ssh


class SocketComm:
    """Wrapper for ZMQ sockets with optional SSH tunnelling.

    Attributes:
        context (zmq.Context): ZMQ Context.
        socket (zmq.Socket): ZMQ Socket.
    """

    def __init__(
        self,
        context: zmq.Context,
        addr: str,
        socket_type: int,
        connect_type: int,
        ssh_server: str = "",
        name: str = "",
    ) -> None:

        self.addr = addr
        self.socket_type = socket_type
        self.connect_type = connect_type
        self.context = context
        self.ssh_server = ssh_server
        self.name = name
        self.socket = self._get_socket()
        self._connect()

    def _get_socket(self) -> zmq.Socket:
        """Creates and returns a ZMQ Socket.

        Raises:
            ValueError: If `socket_type` is not one of:
              - `SocketType.PUSH`
              - `SocketType.PULL`
              - `SocketType.PAIR`
              - `SocketType.PUB`
              - `SocketType.SUB`

        Returns:
            socket (zmq.Socket): A ZMQ Socket.
        """
        if self.socket_type == SocketType.PUSH:
            socket = self.context.socket(zmq.PUSH)

        elif self.socket_type == SocketType.PULL:
            socket = self.context.socket(zmq.PULL)

        elif self.socket_type == SocketType.PAIR:
            socket = self.context.socket(zmq.PAIR)

        elif self.socket_type == SocketType.PUB:
            socket = self.context.socket(zmq.PUB)

        elif self.socket_type == SocketType.SUB:
            socket = self.context.socket(zmq.SUB)
            socket.setsockopt(zmq.SUBSCRIBE, b"")

        else:
            raise ValueError(f"Invalid `socket_type`: {self.socket_type}")
        return socket

    def _connect(self) -> None:
        """Setup the connection.

        https://pyzmq.readthedocs.io/en/latest/howto/ssh.html
        https://stackoverflow.com/a/22474105

        Raises:
            ValueError: If `connect_type` is not one of:
              - `ConnType.BIND`
              - `ConnType.CONNECT`
        """
        if self.ssh_server:
            ssh.tunnel_connection(self.socket, self.addr, self.ssh_server)
            return
        if self.connect_type == ConnType.BIND:
            self.socket.bind(self.addr)
        elif self.connect_type == ConnType.CONNECT:
            self.socket.connect(self.addr)
        else:
            raise ValueError(f"Invalid `connect_type`: {self.connect_type}")


@unique
class SocketType(IntEnum):
    """Socket type enumeration to be used with :py:class:`SocketComm`."""

    PUSH = 0
    PULL = 1
    PAIR = 2
    PUB = 3
    SUB = 4


@unique
class ConnType(IntEnum):
    """Connection type enumeration to be used with :py:class:`SocketComm`."""

    BIND = 0
    CONNECT = 1
