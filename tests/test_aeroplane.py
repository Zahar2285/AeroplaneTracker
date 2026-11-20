import pytest

from src.aeroplane import Aeroplane


def test_aeroplane_creation() -> None:
    plane = Aeroplane("UAL1621", "USA", 268.79, 10203.18)

    assert plane.callsign == "UAL1621"
    assert plane.origin_country == "USA"
    assert plane.velocity == 268.79
    assert plane.altitude == 10203.18


def test_aeroplane_invalid_callsign() -> None:
    with pytest.raises(ValueError):
        Aeroplane("", "USA", 250, 9000)


def test_aeroplane_invalid_country() -> None:
    with pytest.raises(ValueError):
        Aeroplane("UAL1621", "", 250, 9000)


def test_aeroplane_invalid_velocity() -> None:
    with pytest.raises(ValueError):
        Aeroplane("UAL1621", "USA", -10, 9000)


def test_aeroplane_invalid_altitude() -> None:
    with pytest.raises(ValueError):
        Aeroplane("UAL1621", "USA", 250, -100)


def test_is_faster_than() -> None:
    plane1 = Aeroplane("A1", "USA", 300, 9000)
    plane2 = Aeroplane("B1", "Germany", 250, 10000)

    assert plane1.is_faster_than(plane2) is True


def test_is_higher_than() -> None:
    plane1 = Aeroplane("A1", "USA", 300, 12000)
    plane2 = Aeroplane("B1", "Germany", 250, 10000)

    assert plane1.is_higher_than(plane2) is True


def test_aeroplane_invalid_icao24() -> None:
    with pytest.raises(ValueError):
        Aeroplane("UAL1621", "USA", 250, 9000, "")


def test_is_faster_than_without_velocity() -> None:
    plane1 = Aeroplane("A1", "USA", None, 9000)
    plane2 = Aeroplane("B1", "Germany", 250, 10000)

    with pytest.raises(ValueError):
        plane1.is_faster_than(plane2)


def test_is_higher_than_without_altitude() -> None:
    plane1 = Aeroplane("A1", "USA", 250, None)
    plane2 = Aeroplane("B1", "Germany", 270, 10000)

    with pytest.raises(ValueError):
        plane1.is_higher_than(plane2)


def test_cast_to_object_list() -> None:
    data = [
        {
            "callsign": "UAL1621",
            "origin_country": "USA",
            "velocity": 268.79,
            "baro_altitude": 10203.18,
            "icao24": "abc123",
        }
    ]

    result = Aeroplane.cast_to_object_list(data)

    assert len(result) == 1
    assert result[0].callsign == "UAL1621"
    assert result[0].origin_country == "USA"
    assert result[0].velocity == 268.79
    assert result[0].altitude == 10203.18
    assert result[0].icao24 == "abc123"


def test_cast_to_object_list_with_missing_data() -> None:
    data = [{}]

    result = Aeroplane.cast_to_object_list(data)

    assert result[0].callsign == "Unknown"
    assert result[0].origin_country == "Unknown"
    assert result[0].velocity is None
    assert result[0].altitude is None
    assert result[0].icao24 == "unknown"


def test_cast_to_object_list_empty() -> None:
    assert Aeroplane.cast_to_object_list([]) == []
