
from typing import Any


class Aeroplane:
    """Класс для хранения информации о самолёте."""

    def __init__(
        self,
        callsign: str,
        origin_country: str,
        velocity: float | None,
        altitude: float | None,
        icao24: str = "unknown",
    ) -> None:
        if not isinstance(callsign, str) or not callsign.strip():
            raise ValueError("Позывной должен быть непустой строкой")

        if not isinstance(origin_country, str) or not origin_country.strip():
            raise ValueError("Страна регистрации должна быть указана")

        if not isinstance(icao24, str) or not icao24.strip():
            raise ValueError("Идентификатор самолёта должен быть указан")

        if velocity is not None and (
            not isinstance(velocity, (int, float)) or velocity < 0
        ):
            raise ValueError("Скорость должна быть неотрицательным числом")

        if altitude is not None and (
            not isinstance(altitude, (int, float)) or altitude < 0
        ):
            raise ValueError("Высота должна быть неотрицательным числом")

        self.__callsign = callsign.strip()
        self.__origin_country = origin_country.strip()
        self.__velocity = velocity
        self.__altitude = altitude
        self.__icao24 = icao24.strip()

    @property
    def callsign(self) -> str:
        return self.__callsign

    @property
    def origin_country(self) -> str:
        return self.__origin_country

    @property
    def velocity(self) -> float | None:
        return self.__velocity

    @property
    def altitude(self) -> float | None:
        return self.__altitude

    @property
    def icao24(self) -> str:
        return self.__icao24

    def is_faster_than(self, other: "Aeroplane") -> bool:
        """Проверяет, быстрее ли этот самолёт другого."""
        if self.velocity is None or other.velocity is None:
            raise ValueError("Недостаточно данных для сравнения скорости")
        return self.velocity > other.velocity

    def is_higher_than(self, other: "Aeroplane") -> bool:
        """Проверяет, летит ли этот самолёт выше другого."""
        if self.altitude is None or other.altitude is None:
            raise ValueError("Недостаточно данных для сравнения высоты")
        return self.altitude > other.altitude

    @classmethod
    def cast_to_object_list(
        cls, aeroplanes: list[dict[str, Any]]
    ) -> list["Aeroplane"]:
        """Преобразует список словарей в список объектов самолётов."""
        result = []

        for item in aeroplanes:
            result.append(
                cls(
                    callsign=item.get("callsign") or "Unknown",
                    origin_country=item.get("origin_country") or "Unknown",
                    velocity=item.get("velocity"),
                    altitude=item.get("baro_altitude"),
                    icao24=item.get("icao24") or "unknown",
                )
            )

        return result
