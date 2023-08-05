"""gateway related stuff"""
import asyncio
from abc import ABC
from typing import Union, List

from .api import _Req
from .receiver import Receiver
from .requester import HTTPRequester


class Gateway:
    """
    Component which deals with network connection and package send/receive

    reminder: this is not AsyncRunnable cuz gateway dose not have its own tasks, only pass loop to _in/_out
    """
    requester: HTTPRequester
    receiver: Receiver

    def __init__(self, requester: HTTPRequester, receiver: Receiver):
        self.requester = requester
        self.receiver = receiver

    async def request(self, method: str, route: str, **params) -> Union[dict, list]:
        """execute raw request, this is just a wrapper for convenience"""
        return await self.requester.request(method, route, **params)

    async def exec_req(self, r: _Req):
        """execute request, this is just a wrapper for convenience"""
        return await self.requester.exec_req(r)

    async def exec_paged_req(self, r: _Req, **kwargs) -> List:
        """execute paged request, this is just a wrapper for convenience"""
        return await self.requester.exec_paged_req(r, **kwargs)

    async def run(self, in_queue: asyncio.Queue):
        """run the receiver"""
        self.receiver.pkg_queue = in_queue
        await self.receiver.start()


class Requestable(ABC):
    """
    Classes that can use a `Gateway` to communicate with khl server.

    For example:
        `Message`: can use msg.reply() to send a reply to khl

        `Guild`: guild.get_roles() to fetch role list from khl
    """
    gate: Gateway
