import pytest

from infrastructure.models import Apartment, House


class TestCase:
    apartment_endpoint = "/api/v1/apartments/"
    test_input_data_apartment = {
        "number": 1,
        "area": 64,
    }

    @pytest.mark.django_db(transaction=True)
    def test_list_apartment(self, client, water_meter_data):
        response = client.get(self.apartment_endpoint)
        print(response.json())
        assert response.status_code == 200, (
            f"Проверьте, что при обращении к {self.apartment_endpoint}"
            " пользователь получает код 200"
        )

    @pytest.mark.django_db(transaction=True)
    def test_post_apartment(self, client, water_meter_data):
        self.test_input_data_apartment.update({
            'house': House.objects.first().id
        })
        obj_count = Apartment.objects.count()
        response = client.post(
            self.apartment_endpoint,
            data=self.test_input_data_apartment,
            content_type="application/json",
        )
        assert response.status_code == 201, (
            "Проверьте, что при создании объекта через"
            f" {self.apartment_endpoint} пользователь получает код 201",
            str(response)
        )
        assert obj_count + 1 == Apartment.objects.count()
