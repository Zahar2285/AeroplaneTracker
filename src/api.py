
from abc import ABC, abstractmethod


class BaseAPI(ABC):
    """Абстрактный класс для работы с внешними API."""

    @abstractmethod
    def get_country_coordinates(self, country: str) -> list:
        """Получает координаты страны."""
        pass

    @abstractmethod
    def get_aeroplanes(self, country: str) -> list:
        """Получает список самолётов в воздушном пространстве страны."""
        pass
