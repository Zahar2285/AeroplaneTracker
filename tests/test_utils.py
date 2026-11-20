
import pytest

from src.aeroplane import Aeroplane
from src.utils import filter_by_country, get_top_n, sort_by_altitude


@pytest.fixture
def aeroplanes() -> list[Aeroplane]:
    return [
        Aeroplane("A1", "USA", 250, 9000),
        Aeroplane("B1", "Germany", 270, 12000),
        Aeroplane("C1", "USA", 230, 7000),
        Aeroplane("D1", "France", 240, None),
    ]


def test_filter_by_country(aeroplanes: list[Aeroplane]) -> None:
    result = filter_by_country(aeroplanes, ["USA"])

    assert len(result) == 2
    assert all(plane.origin_country == "USA" for plane in result)


def test_filter_by_country_case_insensitive(
    aeroplanes: list[Aeroplane],
) -> None:
    result = filter_by_country(aeroplanes, ["usa"])

    assert len(result) == 2


def test_sort_by_altitude(aeroplanes: list[Aeroplane]) -> None:
    result = sort_by_altitude(aeroplanes)

    assert [plane.callsign for plane in result] == [
        "B1", "A1", "C1", "D1"
    ]


def test_get_top_n(aeroplanes: list[Aeroplane]) -> None:
    result = get_top_n(aeroplanes, 2)

    assert [plane.callsign for plane in result] == ["B1", "A1"]


def test_get_top_n_zero(aeroplanes: list[Aeroplane]) -> None:
    assert get_top_n(aeroplanes, 0) == []


def test_get_top_n_negative(aeroplanes: list[Aeroplane]) -> None:
    with pytest.raises(ValueError):
        get_top_n(aeroplanes, -1)
