""" Math callback API responses """

from callbacks.callback import Callback
from packages.queueing.queueing import Queueing
from packages.queueing.threading import Threading

from models.response_model import ResponseModel, ErrorModel
from models.math_model import SumMathModel
from functions.math_function import MathFunction


class MathCallback:
    """
    Math callback API responses class

    methods:
        sum_callback(body) -> None
    """

    @classmethod
    async def sum_callback(cls, body: SumMathModel) -> None:
        """
        Sum callback API response

        :param body: sum math api request body
        :return: None
        """
        Threading.begin_process()
        try:
            sum_ = await MathFunction.sum(body.numbers)
            result = {
                'sum': sum_
            }

            response = ResponseModel(statusCode=200, statusText='OK', result=result)

            await Callback.send_callback(body.callbackUrl, response.__dict__)
        except Exception as exc:  # pylint: disable=W0718
            error = {
                "type": type(exc).__name__,
                "loc": [],
                "msg": str(exc).capitalize(),
                "input": body.__dict__
            }

            response = ErrorModel(statusCode=500, statusText='Internal Server Error', error=error)

            await Callback.send_callback(body.callbackUrl, response.__dict__)
        Threading.end_process()

        await Queueing.check_queue()
