""" Model for API responses """

from pydantic import BaseModel


class ResponseModel(BaseModel):
    """
    Successful API response model

    attributes:
        statusCode: HTTP status code
        statusText: HTTP status code description
        result: The API result
    """
    statusCode: int
    statusText: str
    result: dict


class ErrorModel(BaseModel):
    """
    Unsuccessful API response model

    attributes:
        statusCode: HTTP status code
        statusText: HTTP status code description
        error: The API error data
    """
    statusCode: int
    statusText: str
    error: dict
