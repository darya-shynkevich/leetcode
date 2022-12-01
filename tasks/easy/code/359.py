# Design a logger system that receives a stream of messages along with their timestamps.
# Each unique message should only be printed at most every 10 seconds
# (i.e. a message printed at timestamp t will prevent other identical messages
# from being printed until timestamp t + 10).
#
# All messages will come in chronological order.
# Several messages may arrive at the same timestamp.
#
# Implement the Logger class:
#
# Logger() Initializes the logger object.
# bool shouldPrintMessage(int timestamp, string message)
# Returns true if the message should be printed in the given timestamp, otherwise returns false.

# Constraints:
#
# 0 <= timestamp <= 109
# Every timestamp will be passed in non-decreasing order (chronological order).
# 1 <= message.length <= 30
# At most 104 calls will be made to shouldPrintMessage.


# Runtime: O(1), Space: O(n)
class Logger:
    def __init__(self):
        self.locker = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        expire_at = self.locker.get(message)
        if expire_at is None or (expire_at and timestamp >= expire_at):
            self.locker[message] = timestamp + 10
            return True
        return False


# Runtime: O(n), Space: O(m)
# class Logger:
#
#     def __init__(self):
#         self.history = set()
#         self.queue = list()
#
#     def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
#         while self.queue and self.queue[0][0] <= timestamp - 10:
#             self.history.remove(self.queue[0][1])
#             self.queue.pop(0)
#
#         if message in self.history:
#             return False
#         else:
#             self.history.add(message)
#             self.queue.append((timestamp, message))
#             return True

# Runtime: O(n * m), Memory: O(m)
# class Logger:
#
#     def __init__(self):
#         self.locker = {}
#         self.last_timestamp = 0
#
#     def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
#         expire_at = self.locker.get(message)
#         if self.last_timestamp != timestamp:
#             for key, value in self.locker.items():
#                 if value <= timestamp - 10:
#                     del self.locker[key]
#             self.last_timestamp = timestamp
#
#         if expire_at is None or (expire_at and timestamp >= expire_at):
#             self.locker[message] = timestamp + 10
#             return True
#         return False


if __name__ == "__main__":
    logger = Logger()

    assert logger.shouldPrintMessage(1, "foo") is True
    assert logger.shouldPrintMessage(2, "bar") is True
    assert logger.shouldPrintMessage(3, "foo") is False
    assert logger.shouldPrintMessage(8, "bar") is False
    assert logger.shouldPrintMessage(10, "foo") is False
    assert logger.shouldPrintMessage(11, "foo") is True

    logger = Logger()

    assert logger.shouldPrintMessage(100, "bug") is True
    assert logger.shouldPrintMessage(111, "bug") is True
