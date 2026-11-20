
from src.aeroplane import Aeroplane


def filter_by_country(
    aeroplanes: list[Aeroplane],
    countries: list[str],
) -> list[Aeroplane]:
    """Фильтрует самолёты по странам регистрации."""
    return [
        aeroplane
        for aeroplane in aeroplanes
        if aeroplane.origin_country.lower() in [
            country.lower() for country in countries
        ]
    ]


def sort_by_altitude(
    aeroplanes: list[Aeroplane],
) -> list[Aeroplane]:
    """Сортирует самолёты по высоте по убыванию."""
    return sorted(
        aeroplanes,
        key=lambda aeroplane: (
            aeroplane.altitude is not None,
            aeroplane.altitude if aeroplane.altitude is not None else 0,
        ),
        reverse=True,
    )


def get_top_n(
    aeroplanes: list[Aeroplane],
    n: int,
) -> list[Aeroplane]:
    """Возвращает N самолётов с наибольшей высотой."""
    if n < 0:
        raise ValueError("Количество самолётов не может быть отрицательным")

    return sort_by_altitude(aeroplanes)[:n]
