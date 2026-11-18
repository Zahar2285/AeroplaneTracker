
from abc import ABC, abstractmethod
from typing import Any

import requests


class BaseAPI(ABC):
    """Абстрактный класс для работы с внешними API."""

    @abstractmethod
    def get_country_coordinates(self, country: str) -> list[float]:
        """Получает координаты страны."""
        pass

    @abstractmethod
    def get_aeroplanes(self, country: str) -> list[dict[str, Any]]:
        """Получает список самолётов в воздушном пространстве страны."""
        pass


class AeroplanesAPI(BaseAPI):
    """Класс для получения информации о самолётах через API."""

    def __init__(self) -> None:
        self.nominatim_url = "https://nominatim.openstreetmap.org/search"
        self.opensky_url = "https://opensky-network.org/api/states/all"
        self.headers = {
            "User-Agent": "AeroplaneTracker/1.0"
        }

    def get_country_coordinates(self, country: str) -> list[float]:
        """Получает границы страны из Nominatim."""

        params = {
            "country": country,
            "format": "json",
            "limit": 1,
        }

        try:
            response = requests.get(
                self.nominatim_url,
                params=params,
                headers=self.headers,
                timeout=10,
            )
            response.raise_for_status()
            data = response.json()

            if not data:
                raise ValueError(f"Страна не найдена: {country}")

            boundingbox = data[0]["boundingbox"]

            return [float(value) for value in boundingbox]

        except requests.RequestException as error:
            raise ConnectionError(
                "Не удалось получить координаты страны"
            ) from error
        except (KeyError, TypeError, ValueError) as error:
            raise ValueError(
                f"Не удалось обработать координаты страны: {country}"
            ) from error

    def get_aeroplanes(self, country: str) -> list[dict[str, Any]]:
        """Получает самолёты из OpenSky."""

        south, north, west, east = self.get_country_coordinates(country)

        params = {
            "lamin": south,
            "lamax": north,
            "lomin": west,
            "lomax": east,
        }

        try:
            response = requests.get(
                self.opensky_url,
                params=params,
                timeout=10,
            )
            response.raise_for_status()
            data = response.json()

            states = data.get("states") or []
            aeroplanes = []

            for state in states:
                if len(state) < 12:
                    continue
                    continue

                aeroplanes.append({
                    "icao24": state[0],
                    "callsign": state[1].strip() if state[1] else None,
                    "origin_country": state[2],
                    "longitude": state[5],
                    "latitude": state[6],
                    "baro_altitude": state[7],
                    "on_ground": state[8],
                    "velocity": state[9],
                    "true_track": state[10],
                    "vertical_rate": state[11],
                })

            return aeroplanes

        except requests.RequestException as error:

            raise ConnectionError(

                f"Не удалось получить информацию о самолётах: {error}"

            ) from error
