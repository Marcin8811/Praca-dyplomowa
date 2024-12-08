import logging
import allure
from requests import Response
from utils.checker import Checker
from utils.api import Google_maps_api

# Ustawienia logowania
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@allure.epic("Test Google Maps API")
class TestGoogleMapsAPI:

    @allure.description("Test tworzenia nowego miejsca")
    def test_create_new_place(self):
        logging.info("Metoda POST: Tworzenie nowego miejsca")
        result_post = Google_maps_api.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get("place_id")

        # Sprawdzamy kod statusu i inne parametry
        Checker.check_status_code(result_post, 200)
        Checker.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        Checker.check_json_value(result_post, 'status', 'OK')

        # Zwracamy place_id do wykorzystania w kolejnych testach
        assert place_id is not None, "place_id nie powinno być None"
        logging.info(f"Utworzono nowe miejsce z place_id: {place_id}")
        return place_id

    @allure.description("Test pobierania nowego miejsca")
    def test_get_new_place(self):
        logging.info("Metoda GET: Pobieranie informacji o nowym miejscu")
        place_id = "some_existing_place_id"  # Zastąp prawdziwym place_id
        result_get: Response = Google_maps_api.get_new_place(place_id)

        # Sprawdzamy kod statusu i obecność wymaganych pól
        Checker.check_status_code(result_get, 200)
        Checker.check_json_token(result_get,
                                 ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website',
                                  'language'])
        Checker.check_json_value(result_get, 'address',
                                 '29, side layout,cohen 09')  # Zakładając, że to jest początkowy adres

    @allure.description("Test aktualizacji miejsca")
    def test_update_place(self):
        logging.info("Metoda PUT: Aktualizacja informacji o miejscu")
        place_id = "some_existing_place_id"  # Zastąp prawdziwym place_id
        result_put: Response = Google_maps_api.put_new_place(place_id)

        # Sprawdzamy kod statusu i komunikat o pomyślnej aktualizacji
        Checker.check_status_code(result_put, 200)
        Checker.check_json_token(result_put, ['msg'])
        Checker.check_json_value(result_put, 'msg', 'Address successfully updated')

    @allure.description("Test usuwania miejsca")
    def test_delete_place(self):
        logging.info("Metoda DELETE: Usuwanie miejsca")
        place_id = "some_existing_place_id"  # Zastąp prawdziwym place_id
        result_delete: Response = Google_maps_api.delete_new_place(place_id)

        # Sprawdzamy kod statusu i komunikat o pomyślnym usunięciu
        Checker.check_status_code(result_delete, 200)
        Checker.check_json_token(result_delete, ['status'])
        Checker.check_json_value(result_delete, 'status', 'OK')

        # Sprawdzamy, czy miejsce zostało usunięte
        result_get: Response = Google_maps_api.get_new_place(place_id)
        assert result_get.status_code == 404, f"Oczekiwano 404, ale otrzymano {result_get.status_code}"
        logging.info(f"Miejsce z place_id {place_id} zostało pomyślnie usunięte")

    # Negatywne testy

    @allure.description("Test negatywny: Tworzenie miejsca z brakującymi wymaganymi polami")
    def test_create_new_place_negative(self):
        logging.info("Metoda POST: Próba utworzenia nowego miejsca z brakującymi polami")
        invalid_place_data = {
            "location": {"lat": -38.383494, "lng": 33.427362}
            # Pozostawiamy ciało żądania niekompletne
        }
        result_post = Google_maps_api.create_new_place(invalid_place_data)
        Checker.check_status_code(result_post, 400)  # Oczekujemy błędu 400

    @allure.description("Test negatywny: Pobieranie miejsca z nieprawidłowym place_id")
    def test_get_new_place_negative(self):
        logging.info("Metoda GET: Próba pobrania miejsca z nieprawidłowym place_id")
        invalid_place_id = "invalid_place_id"
        result_get = Google_maps_api.get_new_place(invalid_place_id)
        Checker.check_status_code(result_get, 404)  # Oczekujemy błędu 404

    @allure.description("Test negatywny: Aktualizacja miejsca z nieprawidłowym place_id")
    def test_update_place_negative(self):
        logging.info("Metoda PUT: Próba aktualizacji miejsca z nieprawidłowym place_id")
        invalid_place_id = "invalid_place_id"
        result_put = Google_maps_api.put_new_place(invalid_place_id)
        Checker.check_status_code(result_put, 404)  # Oczekujemy błędu 404

    @allure.description("Test negatywny: Usuwanie miejsca z nieprawidłowym place_id")
    def test_delete_place_negative(self):
        logging.info("Metoda DELETE: Próba usunięcia miejsca z nieprawidłowym place_id")
        invalid_place_id = "invalid_place_id"
        result_delete = Google_maps_api.delete_new_place(invalid_place_id)
        Checker.check_status_code(result_delete, 404)  # Oczekujemy błędu 404
