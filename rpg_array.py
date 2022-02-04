import time
from random import randint
from telegram import Update, ChatAction
from telegram.ext import CallbackContext


def osr(update: Update, context: CallbackContext):
    """Genera stats para OSR. Lanza 3d6."""
    context.bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING, timeout=30)
    arr = []
    for i in range(6):  # Tira 3d6 ordena y suma. Repite 6 veces.
        score = []
        for j in range(3):  # Bucle de los 3d6.
            score.append(randint(1, 6))
        score.sort(reverse=True), arr.append(sum(score))
    arr.sort()  # Ordena la puntuación para presentarla.
    time.sleep(5)
    update.message.reply_text(text=f'Tu _array_ para juegos basados en el _OSR, B/X y AD&D_:\n*{arr}* \n\n'
                              f'Se han generado tirando 3d6', parse_mode='MarkdownV2')


def d20(update: Update, context: CallbackContext):
    """Genera stats para d20. Lanza 4d6 rechaza el más bajo."""
    context.bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING, timeout=30)
    arr = []
    for i in range(6):  # Tira 4d6 ordena, descarta el menor y suma. Repite 6 veces.
        score = []
        for j in range(4):  # Bucle de los 4d6.
            score.append(randint(1, 6))
        score.sort(reverse=True), score.pop(), arr.append(sum(score))
    arr.sort()  # Ordena la puntuación para presentarla.
    time.sleep(5)
    update.message.reply_text(text=f'Tu _array_ para juegos basados en _d20_ es:\n*{arr}* \n\n'
                              f'Se han generado tirando 4d6 rechazando el valor más bajo', parse_mode='MarkdownV2')


def microlite3d6(update: Update, context: CallbackContext):
    """Genera stats para Microlite20. Lanza 3d6."""
    context.bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING, timeout=30)
    arr = []
    for i in range(3):  # Tira 3d6 ordena y suma. Repite 3 veces.
        score = []
        for j in range(3):  # Bucle de los 3d6.
            score.append(randint(1, 6))
        score.sort(reverse=True), arr.append(sum(score))
    arr.sort()  # Ordena la puntuación para presentarla.
    time.sleep(5)
    update.message.reply_text(text=f'Tu _array_ para _Microlite20_ y derivados es: *{arr}* \n\n'
                              f'Se han generado tirando 3d6 como en el OSR, B/X y AD&D', parse_mode='MarkdownV2')


def microlite4d6(update: Update, context: CallbackContext):
    """Genera stats para Microlite20. Lanza 4d6 rechaza el más bajo."""
    context.bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING, timeout=30)
    arr = []
    for i in range(3):  # Tira 4d6 ordena, descarta el menor y suma. Repite 6 veces.
        score = []
        for j in range(4):  # Bucle de los 4d6.
            score.append(randint(1, 6))
        score.sort(reverse=True), score.pop(), arr.append(sum(score))
    arr.sort()  # Ordena la puntuación para presentarla.
    time.sleep(5)
    update.message.reply_text(text=f'Tu _array_ para _Microlite20_ y derivados es: *{arr}* \n\n'
                              f'Se han generado tirando 4d6 rechazando el valor más bajo', parse_mode='MarkdownV2')


def coc(update: Update, context: CallbackContext):
    """Lanza las stats de CoC hasta 6ma."""
    context.bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING, timeout=30)
    arr_1, arr_2 = [], []
    edu = []
    for grupo1 in range(5):  # Tira 3d6 y suma. 5 veces. STR, CON, DEX, APP y POW.
        score = []
        for j in range(3):
            score.append(randint(1, 6))
        score.sort(reverse=True), arr_1.append(sum(score))
    for grupo2 in range(3):  # Tira 2d6+6 y suma. 2 veces. SIZ, INT.
        score = []
        for j in range(2):
            score.append(randint(1, 6))
        score.append(6), score.sort(reverse=True), arr_2.append(sum(score))
    for education in range(3):  # Tira 3d6 + 3 para EDU.
        edu.append(randint(1, 6))
    arr_1.sort(), arr_2.sort()
    edu = sum(edu) + 3
    time.sleep(5)
    update.message.reply_text(text=
                              f'Tu array para _STR, CON, DEX, APP y POW_ es:\n*{arr_1}* '
                              f'\n\nTu array para _INT y SIZ_ es:\n*{arr_2}*'
                              f'\n\nTu _EDU_ es: *[{edu}]*'
                              f'\n\nSe han generado usando las tiradas de _Call of Cthulhu 6ª Edición_',
                              parse_mode='MarkdownV2')


def coc7(update: Update, context: CallbackContext):
    """Lanza las stats de CoC 7ma."""
    context.bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING, timeout=30)
    arr_1, arr_2, = [], []
    luck = []
    for grupo1 in range(5):  # Tira 3d6 suma y multiplica. 5 veces. STR, CON, DEX, APP y POW.
        score = []
        for j in range(3):
            score.append(randint(1, 6))
        score.sort(reverse=True), arr_1.append(sum(score) * 5)
    for grupo2 in range(3):  # Tira 2d6+6 suma y multiplica. 3 veces. SIZ, INT y EDU.
        score = []
        for j in range(2):
            score.append(randint(1, 6))
        score.append(6), score.sort(reverse=True), arr_2.append(sum(score) * 5)
    for suerte in range(3):  # Tira 3d6 para Luck.
        luck.append(randint(1, 6))
    arr_1.sort(), arr_2.sort()
    luck = sum(luck) * 5
    time.sleep(5)
    update.message.reply_text(text=
                              f'Tu array para _STR, CON, DEX, APP y POW_ es:\n*{arr_1}* '
                              f'\n\nTu array para _SIZ, INT y EDU_ es:\n*{arr_2}*'
                              f'\n\nTu _LUCK_ es: *[{luck}]*'
                              f'\n\nSe han generado usando las tiradas de _Call of Cthulhu 7ª Edición_',
                              parse_mode='MarkdownV2')
