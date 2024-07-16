import pytest


class TestCase:

    @pytest.mark.django_db(transaction=True)
    def test_house(self, water_meter_data, client):
        response = client.get("/api/v1/house/")
        print(response.json())
        assert 2 == 1, ('aslkfjwr')
