import pytest
from infrastructure.models import WaterMeter, Apartment


class TestCase:
    water_meter_endpoint = "/api/v1/water-meters/"
    test_input_data_water_meter = {
        "serial_number": "874159d208111",
    }

    @pytest.mark.django_db(transaction=True)
    def test_list_water_meter(self, client, water_meter_data):
        response = client.get(self.water_meter_endpoint)
        print(response.json())
        assert response.status_code == 200, (
            f"Проверьте, что при обращении к {self.water_meter_endpoint}"
            " пользователь получает код 200"
        )

    @pytest.mark.django_db(transaction=True)
    def test_post_water_meter(self, client, water_meter_data):
        self.test_input_data_water_meter.update(
            {"apartment": Apartment.objects.first().id}
        )
        obj_count = WaterMeter.objects.count()
        response = client.post(
            self.water_meter_endpoint,
            data=self.test_input_data_water_meter,
            content_type="application/json",
        )
        assert response.status_code == 201, (
            "Проверьте, что при создании объекта через"
            f" {self.water_meter_endpoint} пользователь получает код 201"
        )
        assert WaterMeter.objects.count() == obj_count + 1
