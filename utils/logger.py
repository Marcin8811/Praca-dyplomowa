import datetime
import os
import logging
from requests import Response

# Ustawenia logirowania
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Logger:
    file_name = f"logs/log_" + str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")) + ".log"

    @classmethod
    def write_log_to_file(cls, data: str):
        # Sprawdzamy, czy jest folder dla logów, jeżeli nie ma, to robimy
        os.makedirs(os.path.dirname(cls.file_name), exist_ok=True)
        with open(cls.file_name, 'a', encoding='utf-8') as logger_file:
            logger_file.write(data)
        logging.info(f"Zapisano logi do pliku: {cls.file_name}")

    @classmethod
    def add_request(cls, url: str, method: str):
        test_name = os.environ.get('PYTEST_CURRENT_TEST', 'unknown_test')

        date_to_add = f"\n-----\n"
        date_to_add += f"Test: {test_name}\n"
        date_to_add += f"Czas: {str(datetime.datetime.now())}\n"
        date_to_add += f"Metoda zapytania: {method}\n"
        date_to_add += f"URL zapytania: {url}\n"
        date_to_add += "\n"

        cls.write_log_to_file(date_to_add)
        logging.info(f"Zarejestrowano zapytanie: {method} {url}")

    @classmethod
    def add_response(cls, result: Response):
        cookies_as_dict = dict(result.cookies)
        headers_as_dict = dict(result.headers)

        date_to_add = f"Status odpowiedzi: {result.status_code}\n"
        date_to_add += f"Treść odpowiedzi: {result.text}\n"
        date_to_add += f"Nagłówki odpowiedzi: {headers_as_dict}\n"
        date_to_add += f"Ciasteczka odpowiedzi: {cookies_as_dict}\n"
        date_to_add += f"\n-----\n"

        cls.write_log_to_file(date_to_add)
        logging.info(f"Odpowiedź zapisana: Status: {result.status_code}, Treść: {result.text[:100]}...")  # Przykład skrócenia treści odpowiedzi
