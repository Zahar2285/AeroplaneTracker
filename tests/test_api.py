
from unittest.mock import patch, Mock

from src.api import AeroplanesAPI


def test_get_country_coordinates() -> None:
    api = AeroplanesAPI()

    mock_response = Mock()
    mock_response.json.return_value = [
        {
            "boundingbox": [
                "27.4335",
                "43.9933",
                "-18.3937",
                "4.5919",
            ]
        }
    ]

    with patch("src.api.requests.get", return_value=mock_response):
        result = api.get_country_coordinates("Spain")

    assert result == [27.4335, 43.9933, -18.3937, 4.5919]


def test_get_aeroplanes() -> None:
    api = AeroplanesAPI()

    coordinates_response = Mock()
    coordinates_response.json.return_value = [
        {
            "boundingbox": [
                "27.4335",
                "43.9933",
                "-18.3937",
                "4.5919",
            ]
        }
    ]

    planes_response = Mock()
    planes_response.json.return_value = {
        "states": [
            [
                "abc123",
                "UAL1621",
                "United States",
                0,
                0,
                -9.7,
                38.0,
                9000.0,
                False,
                250.0,
                180.0,
                0.0,
            ]
        ]
    }

    with patch(
        "src.api.requests.get",
        side_effect=[coordinates_response, planes_response],
    ):
        result = api.get_aeroplanes("Spain")

    assert len(result) == 1
    assert result[0]["icao24"] == "abc123"
    assert result[0]["callsign"] == "UAL1621"
    assert result[0]["velocity"] == 250.0
    assert result[0]["baro_altitude"] == 9000.0


import requests
import pytest


def test_nominatim_connection_error() -> None:
    api = AeroplanesAPI()

    with patch(
        "src.api.requests.get",
        side_effect=requests.RequestException("Ошибка соединения"),
    ):
        with pytest.raises(ConnectionError):
            api.get_country_coordinates("Spain")


def test_opensky_connection_error() -> None:
    api = AeroplanesAPI()

    coordinates_response = Mock()
    coordinates_response.json.return_value = [
        {"boundingbox": ["27", "43", "-18", "4"]}
    ]

    with patch(
        "src.api.requests.get",
        side_effect=[
            coordinates_response,
            requests.RequestException("Ошибка соединения"),
        ],
    ):
        with pytest.raises(ConnectionError):
            api.get_aeroplanes("Spain")
