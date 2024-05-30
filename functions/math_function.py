""" Math functions """

import asyncio


class MathFunction:
    """
    Math function class for API requests

    methods:
        sum(numbers) -> result(int)
    """

    @classmethod
    async def sum(cls, numbers: list[int]) -> int:
        """
        Sum of list of integers

        :param numbers: list of integers
        :return: result(int)
        """
        await asyncio.sleep(5)  # as if the sum function consumes 5 seconds
        return sum(numbers)
