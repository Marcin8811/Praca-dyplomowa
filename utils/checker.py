import json
import logging
from requests import Response

# Ustawienia logowania
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class Checker:
    """Metody testowania statusu kodu"""

    @staticmethod
    def check_status_code(response: Response, status_code):
        # Używamy assert w tle
        assert status_code == response.status_code, f"Oczekiwano {status_code}, ale otrzymano {response.status_code}"
        if response.status_code == status_code:
            logging.info(f"Dobrze! Status kod = {response.status_code}")
        else:
            logging.error(f"Nie dobrze! Status kod = {response.status_code}")

    """Metoda sprawdzania obecności wymaganych pól w odpowiedzi na żądanie"""

    @staticmethod
    def check_json_token(response: Response, expected_value):
        token = json.loads(response.text)
        # Sprawdzamy, czy wszystkie wymagane pola są obecne w odpowiedzi
        assert list(
            token) == expected_value, f"Brak wymaganych pól! Oczekiwano {expected_value}, ale otrzymano {list(token)}"
        logging.info("Wszystkie wymagane pola są obecne")

    """Metoda sprawdzania wartości wymaganych pól w odpowiedzi na żądanie"""

    @staticmethod
    def check_json_value(response: Response, field_name, expected_value):
        check = response.json()
        check_info = check.get(field_name)
        # Sprawdzamy wartość pola
        assert check_info == expected_value, f"Oczekiwano {expected_value}, ale otrzymano {check_info}"
        logging.info(f"{field_name} jest poprawne!")

    """Metoda sprawdzania, czy dane słowo znajduje się w wartości konkretnego pola"""

    @staticmethod
    def check_json_search_word_in_value(response: Response, field_name, search_word):
        check = response.json()
        check_info = check.get(field_name)
        # Sprawdzamy, czy słowo znajduje się w wartości pola
        if search_word in check_info:
            logging.info(f"Słowo '{search_word}' jest obecne w polu {field_name}!")
        else:
            logging.error(f"Słowo '{search_word}' nie zostało znalezione w polu {field_name}!")
