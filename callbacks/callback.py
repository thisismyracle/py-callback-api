""" Basic callback """

import json
import requests


class Callback:
    """
    Basic callback class

    methods:
        send_callback(callback_url,response) -> is_sent(bool)
    """

    @classmethod
    async def send_callback(cls, callback_url: str, response: dict) -> bool:
        """
        Send callback to callback_url

        :param callback_url: callback url for sending post request after the processes are done
        :param response: the actual API response
        :return: is_sent(bool)
        """
        try:
            data = json.dumps(response)
            headers = {
                'Content-Type': 'application/json'
            }
            requests.post(callback_url, data=data, headers=headers, timeout=5)
            print(f'Callback sent to `{callback_url}`...')
            return True
        except requests.exceptions.RequestException:
            print(f'Callback failed to sent to `{callback_url}`...')
            return False
