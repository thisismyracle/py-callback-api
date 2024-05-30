""" Model for math API requests """

from pydantic import BaseModel


class SumMathModel(BaseModel):
    """
    Sum request body model

    attributes:
        numbers: list of integers
        callbackUrl: callback url for sending post request after the processes are done
    """
    numbers: list[int]
    callbackUrl: str | None = None
