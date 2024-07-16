import pytest
from infrastructure.models import WaterMeterData, WaterMeter


class TestCase:
    water_meter_data_endpoint = "/api/v1/water-meters/data/"
    test_input_water_meter_data = {"value": 8722, "date": "2002.03.10"}

    @pytest.mark.django_db(transaction=True)
    def test_list_water_meter_data(self, client, water_meter_data):
        response = client.get(self.water_meter_data_endpoint)
        assert response.status_code == 200, (
            f"Проверьте, что при обращении к {self.water_meter_data_endpoint}"
            " пользователь получает код 200"
        )

    @pytest.mark.django_db(transaction=True)
    def test_post_water_meter_data(self, client, water_meter):
        self.test_input_water_meter_data.update(
            {"water_meter": WaterMeter.objects.first().id}
        )
        obj_count = WaterMeterData.objects.count()
        response = client.post(
            self.water_meter_data_endpoint,
            data=self.test_input_water_meter_data,
            content_type="application/json",
        )
        assert response.status_code == 201, (
            "Проверьте, что при создании объекта через "
            f"{self.water_meter_data_endpoint} пользователь получает код 201"
        )
        assert obj_count + 1 == WaterMeterData.objects.count()
