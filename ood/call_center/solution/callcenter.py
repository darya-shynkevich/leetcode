from collections import deque
from loguru import logger
from typing import List

from employees import Employee


class CallCenter:

    def __init__(self, name: str, employees: List[Employee]):
        self.name = name
        self.calls_queue = deque()

        self.employees = Employee.sort_employees(employees)

    async def process_call(self, call):
        self.calls_queue.append(call)

        for employee in self.employees:
            if len(self.calls_queue) == 0:
                return
            elif employee.is_available:
                logger.info(f'Employee {employee.name} is ready to take call {call.uuid}')
                await employee.answer_call(call=self.calls_queue.popleft())
            else:
                logger.warning(f'Nobody is available to take call {call.uuid}. Please wait!')
