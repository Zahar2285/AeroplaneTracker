import json
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any

from src.aeroplane import Aeroplane


class BaseSaver(ABC):
    """Абстрактный класс для работы с хранилищем самолётов."""

    @abstractmethod
    def add_aeroplane(self, aeroplane: Any) -> None:
        """Добавляет самолёт в хранилище."""
        pass

    @abstractmethod
    def get_aeroplanes(self, criteria: dict[str, Any]) -> list[dict[str, Any]]:
        """Получает самолёты по заданным критериям."""
        pass

    @abstractmethod
    def delete_aeroplane(self, aeroplane: Any) -> None:
        """Удаляет самолёт из хранилища."""
        pass


class JSONSaver(BaseSaver):
    """Класс для сохранения информации о самолётах в JSON."""

    def __init__(self, file_path: str = "data/aeroplanes.json") -> None:
        self.file_path = Path(file_path)
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

        if not self.file_path.exists():
            self.file_path.write_text("[]", encoding="utf-8")

    def add_aeroplane(self, aeroplane: Aeroplane) -> None:
        """Добавляет самолёт в JSON-файл."""

        aeroplanes = self.get_aeroplanes({})

        aeroplanes.append({
            "callsign": aeroplane.callsign,
            "origin_country": aeroplane.origin_country,
            "velocity": aeroplane.velocity,
            "altitude": aeroplane.altitude,
            "icao24": aeroplane.icao24,
        })

        self.file_path.write_text(
            json.dumps(aeroplanes, ensure_ascii=False, indent=4),
            encoding="utf-8",
        )

    def get_aeroplanes(self, criteria: dict) -> list[dict]:
        """Возвращает самолёты по заданным критериям."""

        try:
            aeroplanes = json.loads(
                self.file_path.read_text(encoding="utf-8")
            )
        except (json.JSONDecodeError, FileNotFoundError):
            return []

        if not isinstance(aeroplanes, list):
            return []

        for key, value in criteria.items():
            aeroplanes = [
                aeroplane
                for aeroplane in aeroplanes
                if aeroplane.get(key) == value
            ]

        return aeroplanes

    def delete_aeroplane(self, aeroplane: Aeroplane) -> None:
        """Удаляет самолёт из JSON-файла."""

        aeroplanes = self.get_aeroplanes({})

        aeroplanes = [
            item for item in aeroplanes
            if item.get("icao24") != aeroplane.icao24
        ]

        self.file_path.write_text(
            json.dumps(aeroplanes, ensure_ascii=False, indent=4),
            encoding="utf-8",
        )
