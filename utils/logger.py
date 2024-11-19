import datetime
import os
from requests import Response


class Logger():
    file_name = f"logs/log_" + str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")) + " .log"
    @classmethod
    def write_log_to_file(cls, data: str):
        #  Sprzawdzamy, czy jest folder dla logów, jeżeli nie ma, to robimy
        os.makedirs(os.path.dirname(cls.file_name), exist_ok=True)
        with open(cls.file_name, 'a', encoding='utf-8') as logger_file:
            logger_file.write(data)

    @classmethod
    def add_request(cls, url: str, method: str):
        test_name = os.environ.get('PYTEST_CURRENT_TEST', 'unknown_test')

        date_to_add = f"\n-----\n"
        date_to_add += f"Test: {test_name}\n"
        date_to_add += f"Time: {str(datetime.datetime.now())}\n"
        date_to_add += f"Request method: {method}\n"
        date_to_add += f"Request URL: {url}\n"
        date_to_add += "\n"

        cls.write_log_to_file(date_to_add)

    @classmethod
    def add_response(cls, result: Response):
        cookies_as_dict = dict(result.cookies)
        headers_as_dict = dict(result.headers)

        date_to_add = f"Response code: {result.status_code}\n"
        date_to_add += f"Response text: {result.text}\n"
        date_to_add += f"Response headers: {headers_as_dict}\n"
        date_to_add += f"Response cookies: {cookies_as_dict}\n"
        date_to_add += f"\n-----\n"

        cls.write_log_to_file(date_to_add)

