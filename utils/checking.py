"""Metody do testowania naszycg żądań"""
import json

from requests import Response


class Checking():
    """Metod testowania statusu kodu"""
    @staticmethod
    def check_status_code(response: Response, status_code):
        assert status_code == response.status_code
        if response.status_code == status_code:
            print("Dobrze! Status kod = " + str(response.status_code))
        else:
            print("Nie dobrze! Status kod = " + str(response.status_code))

    """Metoda sprawdzania obecności wymaganych pól w odpowiedzi na żądanie"""
    @staticmethod
    def check_json_token(response: Response, expected_value):
        token = json.loads(response.text)
        assert list(token) == expected_value
        print("Wszystkie pola są obecne")

    """Metoda sprawdzania wartości wymaganych pól w odpowiedzi na żądanie"""
    @staticmethod
    def check_json_value(response: Response, field_name, expected_value):
        check = response.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print(field_name + " dobrze!")

    """Metoda sprawdzania wartości wymaganych pól w odpowiedzi na żądanie danym słowem"""
    @staticmethod
    def check_json_search_word_in_value(response: Response, field_name, search_word):
        check = response.json()
        check_info = check.get(field_name)
        if search_word in check_info:
            print("Słowę " + search_word + " jest!")
        else:
            print("Słowę " + search_word + " nie ma!")

