""" Router for math requests """

from fastapi import APIRouter

from models.math_model import SumMathModel
from models.response_model import ResponseModel, ErrorModel

from functions.math_function import MathFunction
from packages.queueing.queueing import Queueing
from callbacks.math_callback import MathCallback


router = APIRouter()


@router.post('/math/sum/')
async def math_sum(body: SumMathModel):
    """
    POST /math/sum/

    headers:
    -

    body:
    numbers: array of integer
    callbackUrl: callback url (optional)
    """
    if body.numbers is None or len(list(body.numbers)) == 0:
        # no numbers provided
        status_code = 400
        status_text = 'Bad Request'
        error = {
            'message': 'No numbers provided'
        }
        return ErrorModel(statusCode=status_code, statusText=status_text, error=error)

    if False in (str(num).isnumeric() for num in body.numbers):
        # there is a NaN value among the numbers
        status_code = 400
        status_text = 'Bad Request'
        error = {
            'message': 'There is a NaN value among the numbers'
        }
        return ErrorModel(statusCode=status_code, statusText=status_text, error=error)

    if body.callbackUrl is None:
        # without callback
        status_code = 200
        status_text = 'OK'
        result = {
            'sum': await MathFunction.sum(body.numbers)
        }
        return ResponseModel(statusCode=status_code, statusText=status_text, result=result)

    # with callback
    is_direct = await Queueing.add_to_queue(MathCallback.sum_callback, body)

    status_code = 200
    status_text = 'OK'
    queue_message = 'Please wait... your task is currently at queue.'
    if is_direct:
        queue_message = 'Please wait... your task is directly processed.'
    result = {
        'message': queue_message,
        'callbackUrl': body.callbackUrl
    }
    return ResponseModel(statusCode=status_code, statusText=status_text, result=result)
