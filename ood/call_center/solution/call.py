import asyncio
import uuid
from loguru import logger


class CallStatus:
    PENDING = 0
    ANSWERED = 1


class Call:

    def __init__(self):
        self.uuid = uuid.uuid4()
        self.status = CallStatus.PENDING

    @property
    def is_pending(self):
        return self.status == CallStatus.PENDING

    async def mark_as_answered(self):
        await asyncio.sleep(1)
        self.status = CallStatus.ANSWERED
        logger.info(f'Call {self.uuid} has been answered')
