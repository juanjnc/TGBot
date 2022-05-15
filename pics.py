import os
from random import choice
from telegram import Update, ChatAction
from telegram.ext import CallbackContext


def nohorny(update: Update, context: CallbackContext):
    """Envía un meme de Horny Police al azar. Mauro y Belen pueden sacar nada. Juanjo es Horny"""
    user = update.effective_user
    directory = './pics/noh/'
    noh = choice(os.listdir(directory))
    try:
        context.bot.deleteMessage(chat_id=update.message.chat_id, message_id=update.message.message_id)
        context.bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.UPLOAD_PHOTO, timeout=10)
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(directory + noh, 'rb'))
    except Exception:
        context.bot.send_message(chat_id=update.effective_chat.id, text='No tengo permisos para esto')


def nocombat(update: Update, context: CallbackContext):
    """Envía una imagen wholesome al azar."""
    try:
        context.bot.deleteMessage(chat_id=update.message.chat_id, message_id=update.message.message_id)
        context.bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.UPLOAD_PHOTO, timeout=10)
        directory = './pics/noc/'
        noc = choice(os.listdir(directory))
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(directory + noc, 'rb'))
    except Exception:
        context.bot.send_message(chat_id=update.effective_chat.id, text='No tengo permisos para esto')
