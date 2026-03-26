from pr_14_3_bot_media import *
from L_03_db import *


admin_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Пользователи', callback_data='users')],
        [InlineKeyboardButton(text='Статистика', callback_data='stat')],
        [
            InlineKeyboardButton(text='Блокировать', callback_data='block'),
            InlineKeyboardButton(text='Разблокировать', callback_data='unblock')
        ]
    ]
)