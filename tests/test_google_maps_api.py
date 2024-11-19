import json
import allure
from requests import Response
from utils.checking import Checking
from utils.api import Google_maps_api

"""Tworzenie, zmiana i usunięcie nowej lokalizacji"""
@allure.epic("Test create place")
class TestCreatePlace:
    @allure.description("Test create, update, delete new place")
    def test_create_new_place(self):
        print("Method POST") # Robimy nowe miejsce
        result_post = Google_maps_api.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get("place_id")
        Checking.check_status_code(result_post, 200)
        Checking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        token = json.loads(result_post.text)
        Checking.check_json_value(result_post, 'status', 'OK')

        print("Method GET POST")    # Otrzymujemu info o tworzeniu nowego miejsca
        result_get: Response = Google_maps_api.get_new_place(place_id)
        if result_get is not None:
            Checking.check_status_code(result_get, 200)
        else:
            print("Błąd: result_get wrócił None")
            assert False, "API wrócił None"
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        Checking.check_json_value(result_get, 'address', '29, side layout,cohen 09')

        print("Method PUT")         # Aktualizujemy info o miejscu
        result_put: Response = Google_maps_api.put_new_place(place_id)
        Checking.check_status_code(result_put, 200)
        Checking.check_json_token(result_put, ['msg'])
        Checking.check_json_value(result_put, 'msg', 'Address successfully updated')

        print("Method GET PUT")     # Otrzymujemy aktualizowaną info o miejscu
        result_get: Response = Google_maps_api.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        Checking.check_json_value(result_get, 'address', '100 Lenina street, RU')

        print("Method DELETE")      # Usuwamy miejsce
        result_delete: Response = Google_maps_api.delete_new_place(place_id)
        Checking.check_status_code(result_delete, 200)
        Checking.check_json_token(result_delete, ['status'])
        Checking.check_json_value(result_delete, 'status', 'OK')

        print("Method GET DELETE")     # Sprawdzamy, że miejsce było usuniętę
        result_get: Response = Google_maps_api.get_new_place(place_id)

        # Sprawdzamy, że po usunięciu my otrzymujemy 404 i dobry msg
        if result_get.status_code == 404:
            print("Miesjce usunięto dobrze, otrzymali status 404.")
            print('msg: Get operation failed, looks like place_id doesn\'t exists')
        else:
            print("Błąd: Miejsce nie było usunięte albo wracamy nieczakany status")
            assert False, f"Expected 404, but got {result_get.status_code}"

        # Logika do usunięcia (jeżeli lokalizacja nie istnieje, można wydrukować dodatkowy komunikat)
        if result_delete.status_code == 200:
            print("Usunięcie powiodło się")
        else:
            print("Błąd usuwania, najprawdopodobniej lokalizacja nie istnieje")
            print('msg: Delete operation failed, looks like the data doesn\'t exists')
        Checking.check_json_token(result_put, ['msg'])
        Checking.check_json_search_word_in_value(result_get, 'msg', 'failed')


        print("Testowanie tworzenij, zmian i usunięc nowej lokalizacji skończyło się dobrze!")
