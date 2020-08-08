from parkovadolina.screens.building_progress.constants import BUILDING_STATUS_MAP, STATUS_MAP, STATUS_MAP_SMALL
from parkovadolina.core.screen import Screen
from aiogram import types
from aiogram.types.message import ParseMode

class BuildingProgressScreen(Screen):

    SECTIONS = ["↩️Назад"]

    def __init__(self, bot, dao):
        self.bot = bot
        self.dao = dao
        self.sections = self._build_sections()

    def _build_sections(self):
        return [types.KeyboardButton(i) for i in self.SECTIONS]

    def generate_states(self, done_states, inprogress_states):
        states = ["waiting" for i in range(len(BUILDING_STATUS_MAP))]
        for i in done_states:
            states[i] = "done"
        for i in inprogress_states:
            states[i-1] = "inprogress"
        return "\n".join([f'- {STATUS_MAP_SMALL.get(e)} {BUILDING_STATUS_MAP.get(str(i))}' for i,e in enumerate(states, start=1)])

    def progress_bar(self, progress=4, max_progress=12):
        estimated_line = ["□" for _ in range(max_progress)]
        for i in range(progress):
            estimated_line[i] = "■"
        return "".join(estimated_line)
    
    async def details_header(self, message, building):
        text_body = f'<strong>🏗{building.title.upper()}</strong>'
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        keyboard.row(*[types.KeyboardButton(i) for i in STATUS_MAP.values()])
        keyboard.add(*self.sections)
        await self.bot.send_message(message.chat.id, text_body, reply_markup=keyboard, parse_mode=ParseMode.HTML)

    async def details(self, message, building):
        await self.details_header(message, building)
        progress = [int(i) for i in building.get_expected_state()]
        done_progress = [int(i) for i in range(0, min(progress)-1)]
        progress_percent = round(min(progress) / 12 * 100, 2)
        text_states = self.generate_states(done_progress, progress)
        current_date = building.get_date()
        next_date = building.get_next_date_by_date(current_date)
        prev_date = building.get_prev_date_by_date(current_date)
        text_body = (
            f'<strong>План будівництва на {building.get_date()}:</strong>\n'
            f"{text_states}\n\n"
            f'<strong>|{self.progress_bar(min(progress), 12)}| {progress_percent}%</strong>'
        )
        keyboard_markup = types.InlineKeyboardMarkup(row_width=2)
        row_btns = []
        if prev_date:
            row_btns.append(
                types.InlineKeyboardButton(f'◀️ {prev_date}', callback_data=f'building_{building.title_id}_{prev_date}')
            )
        if next_date:
            row_btns.append(
                types.InlineKeyboardButton(f'{next_date} ▶️', callback_data=f'building_{building.title_id}_{next_date}')
            )
        keyboard_markup.row(*row_btns)
        await self.bot.send_message(message.chat.id, text_body, reply_markup=keyboard_markup, parse_mode=ParseMode.HTML)

    async def in_line(self, query):
        _, title_id, current_date = query.data.split("_")
        building = self.dao.building_plan.get_by_title_id(title_id)
        states_by_date = building.get_state_by_date(current_date)
        progress = [int(i) for i in states_by_date]
        done_progress = [int(i) for i in range(0, min(progress)-1)]
        progress_percent = round(min(progress) / 12 * 100, 2)
        text_states = self.generate_states(done_progress, progress)
        next_date = building.get_next_date_by_date(current_date)
        prev_date = building.get_prev_date_by_date(current_date)
        text_body = (
            f'<strong>План будівництва на {current_date}:</strong>\n'
            f"{text_states}\n\n"
            f'<strong>|{self.progress_bar(min(progress), 12)}| {progress_percent}%</strong>'
        )
        keyboard_markup = types.InlineKeyboardMarkup(row_width=2)
        row_btns = []
        if prev_date:
            row_btns.append(
                types.InlineKeyboardButton(f'◀️ {prev_date}', callback_data=f'building_{building.title_id}_{prev_date}')
            )
        if next_date:
            row_btns.append(
                types.InlineKeyboardButton(f'{next_date} ▶️', callback_data=f'building_{building.title_id}_{next_date}')
            )
        keyboard_markup.row(*row_btns)
        try:
            await self.bot.edit_message_text(
                text_body, 
                chat_id=query.message.chat.id, 
                message_id=query.message.message_id, 
                reply_markup=keyboard_markup, 
                parse_mode=ParseMode.HTML
            )
        except Exception as e:
            print(e)

    async def screen(self, message):
        ctx = self.dao.session.get(message.from_user.id).get_context()
        try:
            building = self.dao.building_plan.get_by_building_title(message.text)
            await self.details(message, building)
        except KeyError:
            building_name = ctx[-1][-1]
            building_stats = message.text
            user_id = message.from_user.id
            self.dao.building_status.create(building_name, building_stats, user_id)
            keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
            keyboard.add(types.KeyboardButton("↩️Назад"))
            await self.bot.send_message(message.chat.id, "Спасибі за ваш внесок", reply_markup=keyboard, parse_mode=ParseMode.HTML)

    def match_context(self, message):
        return message.text in [i for i in STATUS_MAP.values()]

    @staticmethod
    def match(message):
        return message.text.lower().startswith("Будинок".lower()) or False

    @staticmethod
    def in_line_match_pattern(query):
        if query.data.startswith("building_"):
            return True
        return False