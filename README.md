# AeroplaneTracker

## Описание проекта

**AeroplaneTracker** — программа для получения и анализа информации о самолётах, находящихся в воздушном пространстве выбранной страны.

Программа получает географические координаты страны через OpenStreetMap Nominatim API, а затем запрашивает информацию о самолётах через OpenSky API.

Полученные данные сохраняются в JSON-файл и могут сортироваться и фильтроваться.

## Возможности

- Получение координат страны через Nominatim API.
- Получение информации о самолётах через OpenSky API.
- Преобразование полученных данных в объекты класса `Aeroplane`.
- Сохранение информации о самолётах в JSON-файл.
- Поиск самолётов по заданным критериям.
- Удаление самолётов из JSON-хранилища.
- Фильтрация самолётов по стране регистрации.
- Сортировка самолётов по высоте.
- Вывод заданного количества самолётов с наибольшей высотой.

## Используемые технологии

- Python
- Poetry
- Requests
- Python-dotenv
- Pytest
- Pytest-cov
- Flake8
- MyPy
- isort

## Структура проекта

```text
AeroplaneTracker/
├── src/
│   ├── __init__.py
│   ├── api.py
│   ├── aeroplane.py
│   ├── file_saver.py
│   └── utils.py
├── tests/
│   ├── __init__.py
│   ├── test_api.py
│   ├── test_aeroplane.py
│   ├── test_file_saver.py
│   └── test_utils.py
├── data/
├── main.py
├── README.md
├── pyproject.toml
├── poetry.lock
└── .gitignore
```

## Установка

1. Клонировать репозиторий:

```bash
git clone <ссылка-на-репозиторий>
```

2. Перейти в папку проекта:

```bash
cd AeroplaneTracker
```

3. Установить зависимости:

```bash
poetry install
```

## Запуск программы

Для запуска программы выполнить команду:

```bash
poetry run python main.py
```

Далее необходимо указать название страны, количество самолётов для вывода и страны регистрации для фильтрации.

Полученные данные сохраняются в JSON-файл в папке `data`.

## Тестирование

Для запуска тестов:

```bash
poetry run pytest
```

Для проверки покрытия кода тестами:

```bash
poetry run pytest --cov=src --cov-report=term-missing
```

Текущее покрытие кода тестами составляет 91%.

## Проверка качества кода

Для проверки стиля кода:

```bash
poetry run flake8 src tests main.py
```

Для проверки типизации:

```bash
poetry run mypy src main.py
```

Для проверки порядка импортов:

```bash
poetry run isort --check-only src tests main.py
```

## Используемые API

- [OpenStreetMap Nominatim API](https://nominatim.org/release-docs/latest/api/Search/)
- [OpenSky Network API](https://openskynetwork.github.io/opensky-api/rest.html)
