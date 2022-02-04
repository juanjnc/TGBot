import time
from random import choice
from telegram import Update, ChatAction
from telegram.ext import CallbackContext
from datos import razas_erdd, clases_erdd, trasfondos_erdd, razas_13th_age, clases_13th_age, iconos_13th_age


def pjerdd(update: Update, context: CallbackContext):
    """Selecciona las opciones para un PJ de El Resurgir del Dragón"""
    raza = choice(razas_erdd)
    clase = choice(list(clases_erdd.keys()))
    arquetipo = choice(clases_erdd[clase])
    trasfondo = choice(trasfondos_erdd)
    context.bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING, timeout=10)
    time.sleep(5)
    update.message.reply_text(text=f'Tu PJ para _El Resurgir del Dragón_ es:\n\nUn/a *_{raza}_* y se gana la vida como '
                                   f'*_{clase}_*, *_{arquetipo}_* con un pasado de *_{trasfondo}_*\.'
                                   f'\n\nSe incluye _todo el material oficial de NSR_ para generar al PJ\.',
                              parse_mode='MarkdownV2')


def pj13thage(update: Update, context: CallbackContext):
    """Selecciona las opciones para un PJ de 13th Age"""
    raza = choice(razas_13th_age)
    clase = choice(clases_13th_age)
    icono1 = choice(iconos_13th_age)
    icono2 = choice(iconos_13th_age)
    while icono1 == icono2:
        icono2 = choice(iconos_13th_age)
    context.bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING, timeout=10)
    time.sleep(5)
    update.message.reply_text(text=f'Tu PJ para _13th Age_ es:\n\nUn/a *_{raza}_* y se gana la vida como *_{clase}_*\.'
                                   f'\nSeguro que se lo pasa bien con *_{icono1}_* o con *_{icono2}_*\.'
                                   f'\n\nSe incluye _13th Age Core_, _13 True Ways_, _Book of Demons_ '
                                   f'y _Dark Pacts & Ancient Secrerts "3pp"_ para generar al PJ\.',
                              parse_mode='MarkdownV2')
