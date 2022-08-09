from telegram import ReplyKeyboardMarkup, InlineKeyboardMarkup

from tgbot.handlers.onboarding.manage_data import SECRET_LEVEL_BUTTON
from tgbot.handlers.onboarding.static_text import EXAM_TITLE, LEADER_LIST


def make_keyboard_for_start_command() -> ReplyKeyboardMarkup:
    buttons = [
        [EXAM_TITLE],
        [LEADER_LIST]
    ]

    return ReplyKeyboardMarkup(buttons)
