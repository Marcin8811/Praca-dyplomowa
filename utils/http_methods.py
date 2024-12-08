import logging
import requests
from utils.logger import Logger

# Ustawenia logirowania
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Http_methods:
    headers = {'Content-Type': 'application/json'}
    cookie = ""

    @staticmethod
    def get(url):
        logging.info(f"Zapytanie GET: {url}")
        result = requests.get(url, headers=Http_methods.headers, cookies=Http_methods.cookie)
        logging.info(f"Odpowiedź od GET: {result.status_code} - {result.text}")
        Logger.add_response(result)
        return result

    @staticmethod
    def post(url, body):
        logging.info(f"Zapytanie POST: {url}")
        result = requests.post(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookie)
        logging.info(f"Odpowiedź od POST: {result.status_code} - {result.text}")
        Logger.add_response(result)
        return result

    @staticmethod
    def put(url, body):
        logging.info(f"Zapytanie PUT: {url}")
        result = requests.put(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookie)
        logging.info(f"Odpowiedź od PUT: {result.status_code} - {result.text}")
        Logger.add_response(result)
        return result

    @staticmethod
    def delete(url, body):
        logging.info(f"Zapytanie DELETE: {url}")
        result = requests.delete(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookie)
        logging.info(f"Odpowiedź od DELETE: {result.status_code} - {result.text}")
        Logger.add_response(result)
        return result
