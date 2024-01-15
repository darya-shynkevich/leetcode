import abc
import uuid
from enum import Enum
from typing import List

from loguru import logger


class Rank(Enum):
    OPERATOR = 0
    SUPERVISOR = 1
    DIRECTOR = 2


class Employee(abc.ABC):
    def __init__(self, name: str):
        self.name = name
        self.uuid = uuid.uuid4()
        self.is_available = True

    def __hash__(self):
        return hash(str(self))

    def __eq__(self, uuid):
        return self.uuid == uuid

    @staticmethod
    def sort_employees(employees: List['Employee']):
        return sorted(employees, key=lambda employee: employee.RANK.value)

    async def answer_call(self, call):
        if not call.is_pending:
            return

        self.is_available = False

        logger.info(f'Employee {self.name} is answering call {call.uuid} and now is busy')

        await call.mark_as_answered()
        self.is_available = True

        logger.info(f'Employee {self.name} answered call {call.uuid} and now available')


class Operator(Employee):
    RANK = Rank.OPERATOR


class Supervisor(Employee):
    RANK = Rank.SUPERVISOR


class Director(Employee):
    RANK = Rank.DIRECTOR
