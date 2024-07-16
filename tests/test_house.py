import pytest

from infrastructure.models import House, Apartment, WaterMeter, WaterMeterData


class TestCase:
    house_endpoint = "/api/v1/houses/"
    test_input_data_house = {
        "address": "2865 Molina Drive\nBarneschester, PA 01472",
        "name": "rather"
    }

    @pytest.mark.django_db(transaction=True)
    def test_list_house(self, water_meter_data, client):
        response = client.get(self.house_endpoint)
        # assert 2 == 1, str(response)
        assert response.status_code != 404, (
            f"Проверьте, что ендпоинт {self.house_endpoint}"
            " указан в файле urls.py"
        )
        assert response.status_code == 200, (
            f"Проверьте, что при обращении к {self.house_endpoint}"
            " пользователь получает код 200"
        )

    @pytest.mark.django_db(transaction=True)
    def test_post_house(self, client):
        houses_bef = House.objects.count()
        response = client.post(
            self.house_endpoint,
            data=self.test_input_data_house,
        )
        assert response.status_code == 201, (
            f"Проверьте, что при создании объекта через {self.house_endpoint}"
            " пользователь получает код 201"
        )
        assert House.objects.count() == houses_bef + 1
