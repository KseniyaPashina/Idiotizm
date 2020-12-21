import basa
import config
import main
from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

"""Этот файл является дополнительным к файлу main.py
Отвечает за выбор и обработку базы данных."""


A = "a"
B = "b"


def get_keyboard_2():
    """Фунция отвечает за создание кнопок."""
    keyboard = [
        [InlineKeyboardButton("Продолжить", callback_data=A)],
        [InlineKeyboardButton("Закончить", callback_data=B)]
    ]

    return InlineKeyboardMarkup(keyboard)


def keyboard_regulate(update: Update, context):
    """Функция отвечает за реализацию выбора кнопки."""
    callbacks = update.callback_query
    current_callback = callbacks.data

    if current_callback == A:
        number = config.number
        main.end(update, context)
        context.bot.send_message(
            chat_id=update.effective_message.chat_id,
            text="Выбери, что хочешь еще узнать",
            reply_markup=ReplyKeyboardMarkup(get_keyboard(), one_time_keyboard=True)
        )
        config.number = number
        config.flag_begin = False
        config.flag_choose = True
    elif current_callback == B:
        user_name = update.effective_user.first_name
        context.bot.send_message(
            chat_id=update.effective_message.chat_id,
            text=f"Пока, {user_name} \n"
                 f"Надеюсь ты еще вернешься"
        )
        main.end(update, context)


def choose(update: Update, context, text):
    """Функция отвечает за выбор информации, который хочет получить пользоватьль в базе данных.
    Функция реализует кнопки окончательного выбора."""
    number = config.number
    f = True

    if text == "ФИО":
        context.bot.send_message(
            chat_id=update.effective_message.chat_id,
            text=f"{text}: {basa.name.get(number)}"
        )
    elif text == "Номер в группе":
        context.bot.send_message(
            chat_id=update.effective_message.chat_id,
            text=f"{text}: {number} "
        )
    elif text == "Почта ВШЭ":
        context.bot.send_message(
            chat_id=update.effective_message.chat_id,
            text=f"{text}: {basa.email_hse.get(number)}"
        )
    elif text == "Почта МИЭМ":
        context.bot.send_message(
            chat_id=update.effective_message.chat_id,
            text=f"{text}: {basa.email_miem.get(number)}"
        )
    elif text == "Ссылка vk.com":
        context.bot.send_message(
            chat_id=update.effective_message.chat_id,
            text=f"{text}: {basa.vk.get(number)}"
        )
    elif text == "Ссылка instagram.com":
        context.bot.send_message(
            chat_id=update.effective_message.chat_id,
            text=f"{text}: {basa.instagram.get(number)}"
        )
    elif text == "Получить все данные":
        context.bot.send_message(
            chat_id=update.effective_message.chat_id,
            text=f"ФИО: {basa.name.get(number)} \n"
                 f"Почта ВШЭ: {basa.email_hse.get(number)} \n"
                 f"Почта МИЭМ: {basa.email_miem.get(number)} \n"
                 f"Номер в группе: {number} \n"
                 f"Ссылка vk.com: {basa.vk.get(number)} \n"
                 f"Ссылка instagram.com: {basa.instagram.get(number)} \n"
        )
    else:
        context.bot.send_message(
            chat_id=update.effective_message.chat_id,
            text=f"Ошибочка. Начни сначала /end"
        )
        f = False

    if f:
        context.bot.send_message(
            chat_id=update.effective_message.chat_id,
            text=f"Узнать что-то еще об это человеке или закончить?",
            reply_markup=get_keyboard_2()
        )


def check_surname(update: Update, context):
    """Функуия реализует встроенную клавиатура в виде кнопок."""
    update.message.reply_text(
        text="Выбери, что хочешь узнать",
        reply_markup=ReplyKeyboardMarkup(get_keyboard(), one_time_keyboard=True)
    )
    config.flag_choose = True
    config.flag_begin = False


def get_keyboard():
    """Функция создает и возвращает двумерный массив для встроенной клавиатуры.
    Массив отвечает за выбор информации в базе данных"""
    keyboard = [
        ["ФИО"],
        ["Почта ВШЭ"],
        ["Почта МИЭМ"],
        ["Номер в группе"],
        ["Ссылка vk.com"],
        ["Ссылка instagram.com"],
        ["Получить все данные"]
    ]

    return keyboard


