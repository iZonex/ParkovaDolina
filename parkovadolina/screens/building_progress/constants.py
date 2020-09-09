BUILDING_STATUS_MAP = {
    "1": "Котлован",
    "2": "Палі",
    "3": "Фундамент",
    "4": "Монолітний залізобетнний каркас",
    "5": "Стіни, перегородки, покрівля",
    "6": "Внутрішнє оздоблення",
    "7": "Вікна, двері, ліфти",
    "8": "Фасад",
    "9": "Внутрішні інженері мережі",
    "10": "Благоустрій",
    "11": "Зовнішні інженерні мережі",
    "12": "Будивництво завершенно"
}

STATUS_MAP = {
    "1": "✅Все добре",
    "2": "❌Зупинено",
    "3": "❗️Помічені проблеми"
}

STATUS_MAP_SMALL = {
    "done": "✅",
    "waiting": "❌",
    "3": "❗️",
    "inprogress": "▶️",
}

PHOTO_ANGLE = {
    "1.1": "https://parkova-dolyna.com/t/dom-1-rakurs-1-obnovleno-27-08/12",
    "1.2": "https://parkova-dolyna.com/t/dom-1-rakurs-2-obnovleno-27-08/13/4",
    "1.3": "https://parkova-dolyna.com/t/dom-1-rakurs-3-obnovleno-27-08/88/2",
    "1.4": "https://parkova-dolyna.com/t/dom-1-rakurs-4-obnovleno-27-08/14/4",
    "1.5": "https://parkova-dolyna.com/t/dom-1-rakurs-5-obnovleno-27-08/15/4",
    "1.6": "https://parkova-dolyna.com/t/dom-1-rakurs-6-obnovleno-27-08/89/2",
    "2.1": "https://parkova-dolyna.com/t/dom-2-rakurs-1-obnovleno-27-08/90/2",
}


PHOTO_ANGLE_CACHE = [f'<a href="{v}">{k}</a>\n\n' for k,v in PHOTO_ANGLE.items()]