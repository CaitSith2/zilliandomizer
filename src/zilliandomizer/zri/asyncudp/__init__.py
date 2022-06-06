import asyncio
from typing import Any, Optional, Tuple, cast
from .version import version_

__version__ = version_

Address = Tuple[str, int]


class ClosedError(Exception):
    pass


class _SocketProtocol(asyncio.BaseProtocol):

    def __init__(self) -> None:
        self._packets: asyncio.Queue[Optional[Tuple[bytes, Address]]] = asyncio.Queue()

    def connection_made(self, transport: asyncio.BaseTransport) -> None:
        pass

    def connection_lost(self, exc: Optional[Exception]) -> None:
        self._packets.put_nowait(None)

    def datagram_received(self, data: bytes, addr: Address) -> None:
        self._packets.put_nowait((data, addr))

    async def recvfrom(self) -> Optional[Tuple[bytes, Address]]:
        return await self._packets.get()


class Socket:
    """A UDP socket. Use :func:`~asyncudp.create_socket()` to create an
    instance of this class.

    """

    def __init__(self,
                 transport: asyncio.DatagramTransport,
                 protocol: _SocketProtocol) -> None:
        self._transport = transport
        self._protocol = protocol

    def close(self) -> None:
        """Close the socket.

        """

        self._transport.close()

    def sendto(self, data: bytes, addr: Optional[Address] = None) -> None:
        """Send given packet to given address ``addr``. Sends to
        ``remote_addr`` given to the constructor if ``addr`` is
        ``None``.

        >>> sock.sendto(b'Hi!')

        """

        self._transport.sendto(data, addr)

    async def recvfrom(self) -> Tuple[bytes, Address]:
        """Receive a UDP packet.

        Raises ClosedError on connection error, often by calling the
        close() method from another task.

        >>> data, addr = sock.recvfrom()

        """

        packet = await self._protocol.recvfrom()

        if packet is None:
            raise ClosedError()

        return packet

    def getsockname(self) -> Address:
        """Get bound infomation.

        >>> local_address, local_port = sock.getsockname()

        """

        return cast(Address, self._transport.get_extra_info('sockname'))

    async def __aenter__(self) -> "Socket":
        return self

    async def __aexit__(self, *exc_info: Any) -> None:
        self.close()


async def create_socket(local_addr: Optional[Address] = None,
                        remote_addr: Optional[Address] = None) -> Socket:
    """Create a UDP socket with given local and remote addresses.

    >>> sock = await asyncudp.create_socket(local_addr=('127.0.0.1', 9999))

    """
    assert local_addr or remote_addr

    loop = asyncio.get_running_loop()
    transport, protocol = await loop.create_datagram_endpoint(
        _SocketProtocol,
        local_addr=local_addr,
        remote_addr=remote_addr)

    # both mypy and pyright don't see this type
    dgram_transport = cast(asyncio.DatagramTransport, transport)
    # mypy doesn't see this type
    s_protocol = cast(_SocketProtocol, protocol)  # type: ignore

    return Socket(dgram_transport, s_protocol)
