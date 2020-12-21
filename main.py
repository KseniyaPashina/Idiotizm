import config
import basa
import dop
from telegram import Update
from telegram.ext import Updater, MessageHandler, CommandHandler, Filters, CallbackQueryHandler

"""Этот бот является итоговым проектом по дисциплине "Алгоритмизация и программирование".
Бот создан:
студентками группы БИБ203
Павловой Еленой Денисовной
Пашиной Ксенией Игоревной

Файл main.py - Пашина Ксения
Файл dop.py - Павлова Елена """


def message(update: Update, context):
    """Функция отвечает за все входящие сообщения.
    Если сообщение не несет в себе никакого смысла для данного бота, бот выдаст ошибку."""
    if not config.flag_begin and not config.flag_choose:
        context.bot.send_message(
            chat_id=update.effective_message.chat_id,
            text=f"Ознакомьтесь с правилами /help"
        )
    elif config.flag_begin and not config.flag_choose:
        text = update.effective_message.text
        dict = basa.surname
        number = dict.get(text)

        if number is None:
            user_name = update.effective_user.first_name
            context.bot.send_message(
                chat_id=update.effective_message.chat_id,
                text=f"{user_name}, этот человек не числиться в группе БИБ203 или была допущена ошибка в фамилии \n"
                     f"Ознакомьтесь с правилами /help"
            )
        else:
            config.number = number
            dop.check_surname(update, context)
    else:
        text = update.effective_message.text
        dop.choose(update, context, text)


def end(update: Update, context):
    """Функция обнуляет глобальные переменные."""
    config.flag_begin = False
    config.flag_choose = False
    config.number = None


def begin(update: Update, context):
    """Функция отвечает за ввод фамилии студента.
    :param update: отвечает за входящие обновления бота.
    :param context:
    """
    config.flag_begin = True
    context.bot.send_message(
        chat_id=update.effective_message.chat_id,
        text=f"Напиши фамилию студента"
    )


def help(update: Update, context):
    """Функция несет в себе основные команды помощи, а также правила написания сообщений."""
    context.bot.send_message(
        chat_id=update.effective_message.chat_id,
        text=f"Правила: \n"
             f"Фамилия пишется с заглавной буквы в иминительном падеже единственном числе \n"
             f"Чтобы начать воспользуйся командой /begin \n"
             f"Чтобы начать сначала или закончить переписку со мной воспользуйся командой /end"
    )


def start(update: Update, context):
    """Функция является стартовой для бота, приветствует пользователя и предлагает ознакомиться с правилами."""
    user_name = update.effective_user.first_name

    context.bot.send_message(
        chat_id=update.effective_message.chat_id,
        text=f'Привет, {user_name}. Это база данных группы БИБ203'
    )
    context.bot.send_message(
        chat_id=update.effective_message.chat_id,
        text=f"Для начала я предлагаю ознакомиться тебе с правилами. Для этого воспользуйся командой /help \n"
             f"Если ты с ними знаком, воспульзуйся командой /begin"
    )


def test(text):
    """Фунция отвечает за получение ФИО по номеру студента или номера студента по фамилии.
    :param text: строка, являющаяся ключом к одного из двух словарей базы данных.
    :return: значение словаря одной из двух библиотек.
    """
    if text.isalpha():
        return basa.surname.get(text)
    elif text.isdigit():
        return basa.name.get(int(text))
    else:
        return 'error'


def main():
    """Функия является главной и представляет собой связь бота созданного в телеграмме и данного кода.
    Функция создает команды, кнопки и запускает функцию обработки входящих сообщений"""
    my_update = Updater(
        token=config.token,
        base_url=config.proxi,
        use_context=True)

    keyboard = CallbackQueryHandler(
        callback=dop.keyboard_regulate,
        pass_chat_data=True
    )
    my_start = CommandHandler("start", start)
    my_help = CommandHandler("help", help)
    my_begin = CommandHandler("begin", begin)
    my_end = CommandHandler("end", end)
    my_handler = MessageHandler(Filters.all, message)

    my_update.dispatcher.add_handler(my_start)
    my_update.dispatcher.add_handler(my_help)
    my_update.dispatcher.add_handler(my_begin)
    my_update.dispatcher.add_handler(my_end)
    my_update.dispatcher.add_handler(my_handler)
    my_update.dispatcher.add_handler(keyboard)

    my_update.start_polling()
    my_update.idle()




if __name__ == '__main__':
    main()
