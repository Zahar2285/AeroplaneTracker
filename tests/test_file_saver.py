
import json

from src.aeroplane import Aeroplane
from src.file_saver import JSONSaver


def test_add_aeroplane(tmp_path) -> None:
    saver = JSONSaver(str(tmp_path / "aeroplanes.json"))
    plane = Aeroplane("UAL1621", "USA", 268.79, 10203.18, "abc123")

    saver.add_aeroplane(plane)

    result = saver.get_aeroplanes({})

    assert len(result) == 1
    assert result[0]["callsign"] == "UAL1621"


def test_get_aeroplanes_by_country(tmp_path) -> None:
    saver = JSONSaver(str(tmp_path / "aeroplanes.json"))
    plane = Aeroplane("UAL1621", "USA", 268.79, 10203.18, "abc123")

    saver.add_aeroplane(plane)

    result = saver.get_aeroplanes({"origin_country": "USA"})

    assert len(result) == 1


def test_delete_aeroplane(tmp_path) -> None:
    saver = JSONSaver(str(tmp_path / "aeroplanes.json"))
    plane = Aeroplane("UAL1621", "USA", 268.79, 10203.18, "abc123")

    saver.add_aeroplane(plane)
    saver.delete_aeroplane(plane)

    assert saver.get_aeroplanes({}) == []


def test_json_file_is_valid(tmp_path) -> None:
    file_path = tmp_path / "aeroplanes.json"
    saver = JSONSaver(str(file_path))
    plane = Aeroplane("UAL1621", "USA", 268.79, 10203.18, "abc123")

    saver.add_aeroplane(plane)

    with file_path.open(encoding="utf-8") as file:
        data = json.load(file)

    assert isinstance(data, list)
    assert data[0]["icao24"] == "abc123"

