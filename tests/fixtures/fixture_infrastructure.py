import pytest

from tests.fixtures.factories import (
    HouseFactory,
    TariffFactory,
    ApartmentFactory,
    WaterMeterFactory,
    WaterMeterDataFactory,
)


@pytest.fixture
def house():
    return HouseFactory.create_batch(5)


@pytest.fixture
def apartment(house):
    return ApartmentFactory.create_batch(5)


@pytest.fixture
def water_meter(apartment):
    return WaterMeterFactory.create_batch(5)


@pytest.fixture
def water_meter_data():
    return WaterMeterDataFactory.create_batch(5)


@pytest.fixture
def tariff():
    return TariffFactory.create_batch(5)


@pytest.fixture
def anonymous_user(client):
    """Фикстура для анонимного пользователя."""
    client.logout()
    return client


{
    "count": 16,
    "next": None,
    "previous": None,
    "results": [
        {
            "id": 1,
            "address": "68671 Amanda Circle\nNorth Robertshire, TN 85834",
            "name": "head",
            "apartments": [],
        },
        {
            "id": 2,
            "address": "1187 Keith Ford\nLake Benjamin, NV 50867",
            "name": "answer",
            "apartments": [],
        },
        {
            "id": 3,
            "address": "USS Mcguire\nFPO AP 38613",
            "name": "together",
            "apartments": [],
        },
        {
            "id": 4,
            "address": "USNS Tate\nFPO AP 94973",
            "name": "position",
            "apartments": [],
        },
        {
            "id": 5,
            "address": "7456 Sandra Unions Apt. 769\nDouglasport, FM 49718",
            "name": "student",
            "apartments": [],
        },
        {
            "id": 6,
            "address": "726 Craig Court Suite 701\nEast Joseview, MA 84468",
            "name": "security",
            "apartments": [
                {"id": 1, "number": 1, "area": 35, "water_meters": []}
            ],
        },
        {
            "id": 7,
            "address": "864 Simmons Square Suite 868\nNorth Ann, CA 11996",
            "name": "compare",
            "apartments": [
                {"id": 2, "number": 2, "area": 174, "water_meters": []}
            ],
        },
        {
            "id": 8,
            "address": "189 Deborah Mountains\nLake Michelle, KS 57128",
            "name": "indeed",
            "apartments": [
                {"id": 3, "number": 3, "area": 97, "water_meters": []}
            ],
        },
        {
            "id": 9,
            "address": "USS Perez\nFPO AA 52876",
            "name": "well",
            "apartments": [
                {"id": 4, "number": 4, "area": 31, "water_meters": []}
            ],
        },
        {
            "id": 10,
            "address": "Unit 5940 Box 8624\nDPO AP 61052",
            "name": "free",
            "apartments": [
                {"id": 5, "number": 5, "area": 174, "water_meters": []}
            ],
        },
        {
            "id": 11,
            "address": "PSC 1043, Box 3054\nAPO AP 26093",
            "name": "popular",
            "apartments": [
                {
                    "id": 6,
                    "number": 6,
                    "area": 159,
                    "water_meters": [{"serial_number": "1148685562365"}],
                }
            ],
        },
        {
            "id": 12,
            "address": "504 Medina Key Apt. 415\nAmyshire, WI 34255",
            "name": "wrong",
            "apartments": [
                {
                    "id": 7,
                    "number": 7,
                    "area": 163,
                    "water_meters": [{"serial_number": "8581217829254"}],
                }
            ],
        },
        {
            "id": 13,
            "address": "183 Sean Road Apt. 755\nSouth Erin, WI 92324",
            "name": "two",
            "apartments": [
                {
                    "id": 8,
                    "number": 8,
                    "area": 91,
                    "water_meters": [{"serial_number": "0750341727332"}],
                }
            ],
        },
        {
            "id": 14,
            "address": "USS Silva\nFPO AP 17656",
            "name": "improve",
            "apartments": [
                {
                    "id": 9,
                    "number": 9,
                    "area": 118,
                    "water_meters": [{"serial_number": "9224892642693"}],
                }
            ],
        },
        {
            "id": 15,
            "address": "PSC 1947, Box 2065\nAPO AE 39076",
            "name": "suddenly",
            "apartments": [
                {
                    "id": 10,
                    "number": 10,
                    "area": 158,
                    "water_meters": [{"serial_number": "7158946966447"}],
                }
            ],
        },
        {
            "id": 16,
            "address": "94381 Jones Loaf Apt. 257\nNorth Jennifer, NE 58841",
            "name": "chair",
            "apartments": [
                {
                    "id": 11,
                    "number": 11,
                    "area": 61,
                    "water_meters": [{"serial_number": "3293656690252"}],
                }
            ],
        },
    ],
}
