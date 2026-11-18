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
