import asyncio

from callcenter import CallCenter
from employees import Operator, Supervisor, Director
from call import Call


async def main():
    call_center = CallCenter(
        name='My Lovely CallCenter',
        employees=[
            Director(name='Director 1'),
            Operator(name='Operator 1'),
            Operator(name='Operator 1'),
            Operator(name='Operator 1'),
            Supervisor(name='Supervisor 1'),
            Supervisor(name='Supervisor 2'),
        ],
    )

    calls = []
    for i in range(10):
        calls.append(call_center.process_call(call=Call()))

    await asyncio.gather(*calls)


if __name__ == "__main__":
    asyncio.run(main())
