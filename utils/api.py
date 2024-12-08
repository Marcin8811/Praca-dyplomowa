import logging
import requests
from utils.http_methods import Http_methods

# Ustawenia logirowania
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

base_url = "https://rahulshettyacademy.com"  # Bazowy URL
key = '?key=qaclick123'  # Parametr dla wszystkich zapytań


class Google_maps_api:
    """Metody do pracy z Google Maps API"""

    @staticmethod
    def create_new_place():
        """Metoda tworzenia nowego miejsca"""
        json_for_create_new_place = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            },
            "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout,cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }

        post_resource = "/maps/api/place/add/json"  # Zadanie dla zasobu metoda POST
        post_url = base_url + post_resource + key
        logging.info(f"POST URL: {post_url}")  # Logowanie URL

        result_post = Http_methods.post(post_url, json_for_create_new_place)
        logging.info(f"Odpowiedz na POST: {result_post.text}")  # Logowanie tekstu odpowiedzi

        return result_post

    @staticmethod
    def get_new_place(place_id):
        """Metoda dla otrzymanie informacji o miejscu"""
        get_resource = "/maps/api/place/get/json"
        get_url = f"{base_url}{get_resource}{key}&place_id={place_id}"
        logging.info(f"GET URL: {get_url}")  # Logowanie URL zapytania

        # Robimy GET zapytanie
        result_get = requests.get(get_url)

        if result_get.status_code == 200:
            logging.info(f"Odpowiedź od GET API: {result_get.text}")  # Logowanie ciała odpowiedzi
        else:
            logging.error(f"Błąd podczas zapytania GET: {result_get.status_code} - {result_get.text}")

        return result_get

    @staticmethod
    def put_new_place(place_id):
        """Metoda dla aktualizacji informacji o miejscu"""
        put_resource = "/maps/api/place/update/json"
        put_url = base_url + put_resource + key  # Robimy URL dla PUT zapytania
        logging.info(f"PUT URL: {put_url}")  # Logowanie URL zapytania

        json_for_update_new_location = {
            "place_id": place_id,
            "address": "100 Lenina street, RU",  # Nowy adres dla aktualizacji
            "key": "qaclick123"
        }

        result_put = Http_methods.put(put_url, json_for_update_new_location)  # Robimy PUT zapytanie
        logging.info(f"Odpowiedź na PUT: {result_put.text}")  # Logowanie odpowiedzi od serwera

        return result_put

    @staticmethod
    def delete_new_place(place_id):
        """Metoda dla usunięcia miejsca"""
        delete_resource = "/maps/api/place/delete/json"  # Źródło DELETE zapytania
        delete_url = base_url + delete_resource + key  # Robimy URL dla DELETE zapytania
        logging.info(f"DELETE URL: {delete_url}")  # Logowanie URL zapytania

        json_for_delete_new_location = {
            "place_id": place_id
        }

        result_delete = Http_methods.delete(delete_url, json_for_delete_new_location)  # Robimy DELETE zapytanie
        logging.info(f"Odpowiedź na DELETE: {result_delete.text}")  # Logowanie odpowiedzi od serwera

        return result_delete
