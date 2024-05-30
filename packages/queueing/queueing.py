""" Queueing system """

from typing import Any

from packages.queueing.threading import Threading


class Queueing:
    """
    Queueing class for queued processing

    attributes:
        queue: waiting list of (function, *args) that want to be processed next

    methods:
        add_to_queue(function,*args) -> is_processed(bool)
        check_queue() -> None
    """

    queue: list[tuple[Any, Any]] = []

    @classmethod
    async def add_to_queue(cls, function: Any, *args: Any) -> bool:
        """
        Add process to queue

        :param function: the function you want to run
        :param args: the arguments for the function
        :return: is_processed(bool)
        """
        if Threading.is_available():
            Threading.run_async(function, *args)
            return True

        cls.queue.append((function, *args))
        return False

    @classmethod
    async def check_queue(cls) -> None:
        """
        Check the queue if there are any waiting process, pop, and run it

        :return: None
        """
        if len(cls.queue) > 0 and Threading.is_available():
            function, *args = cls.queue.pop()
            Threading.run_async(function, *args)
