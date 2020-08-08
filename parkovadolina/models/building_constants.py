
STATUS_MAP = {
    "1": "✅Все добре",
    "2": "❌Зупинено",
    "3": "❗️Помічені проблеми"
}

BUILDING_NUMBERS = {
    "1": "Будинок №1 Секція №1-3",
    "2": "Будинок №1 Секція №4-6",
    "3": "Будинок №1 Секція №7-9",
    "4": "Будинок №2 Секція №1",
    "5": "Будинок №2 Секція №2",
    "6": "Будинок №2 Секція №3",
    "7": "Будинок №2 Секція №4",
}

BUILDING_NUMBERS_REVERSED = {v: k for k, v in BUILDING_NUMBERS.items()}

STATUS_MAP_REVERSED = {v: k for k, v in STATUS_MAP.items()}
