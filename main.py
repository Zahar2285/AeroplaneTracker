
from src.api import AeroplanesAPI
from src.aeroplane import Aeroplane
from src.file_saver import JSONSaver
from src.utils import filter_by_country, get_top_n


def user_interaction() -> None:
    """Функция взаимодействия с пользователем."""

    api = AeroplanesAPI()
    saver = JSONSaver()

    country = input("Введите название страны: ").strip()

    if not country:
        print("Название страны не может быть пустым.")
        return

    try:
        print("Получаем информацию о самолётах...")

        data = api.get_aeroplanes(country)
        aeroplanes = Aeroplane.cast_to_object_list(data)

        for aeroplane in aeroplanes:
            saver.add_aeroplane(aeroplane)

        print(f"Получено самолётов: {len(aeroplanes)}")

    except (ConnectionError, ValueError) as error:
        print(f"Ошибка получения данных: {error}")
        return

    if not aeroplanes:
        print("Самолёты не найдены.")
        return

    try:
        top_n = int(
            input("Сколько самолётов показать в топе по высоте? ")
        )

        top_aeroplanes = get_top_n(aeroplanes, top_n)

        print("\nТоп самолётов по высоте:")

        for plane in top_aeroplanes:
            print(
                f"{plane.callsign} | "
                f"{plane.origin_country} | "
                f"Высота: {plane.altitude} м | "
                f"Скорость: {plane.velocity} м/с"
            )

    except ValueError as error:
        print(f"Ошибка ввода: {error}")
        return

    countries = input(
        "\nВведите страны регистрации для фильтрации через запятую: "
    ).split(",")

    countries = [country.strip() for country in countries if country.strip()]

    if countries:
        filtered = filter_by_country(aeroplanes, countries)

        print("\nСамолёты по стране регистрации:")

        for plane in filtered:
            print(
                f"{plane.callsign} | "
                f"{plane.origin_country} | "
                f"Высота: {plane.altitude} м"
            )


if __name__ == "__main__":
    user_interaction()

