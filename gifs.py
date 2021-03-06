import os
from random import choice
from telegram import Update, ChatAction
from telegram.ext import CallbackContext


def pug(update: Update, context: CallbackContext):
    """Envía un gif de pugs."""
    try:
        context.bot.deleteMessage(chat_id=update.message.chat_id, message_id=update.message.message_id)
        context.bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.UPLOAD_PHOTO, timeout=10)
        context.bot.send_document(chat_id=update.effective_chat.id, document=open('./gifs/pugs.mp4', 'rb'))
    except Exception:
        context.bot.send_message(chat_id=update.effective_chat.id, text='No tengo permisos para esto')


def dance(update: Update, context: CallbackContext):
    """Envía un gif de un esqueleto bailando."""
    try:
        context.bot.deleteMessage(chat_id=update.message.chat_id, message_id=update.message.message_id)
        context.bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.UPLOAD_PHOTO, timeout=10)
        context.bot.send_document(chat_id=update.effective_chat.id, document=open('./gifs/dance.mp4', 'rb'))
    except Exception:
        context.bot.send_message(chat_id=update.effective_chat.id, text='No tengo permisos para esto')


def nada(update: Update, context: CallbackContext):
    """Envía un gif de que no ha pasado nada."""
    try:
        context.bot.deleteMessage(chat_id=update.message.chat_id, message_id=update.message.message_id)
        context.bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.UPLOAD_PHOTO, timeout=10)
        context.bot.send_document(chat_id=update.effective_chat.id, document=open('./gifs/nada.mp4', 'rb'))
    except Exception:
        context.bot.send_message(chat_id=update.effective_chat.id, text='No tengo permisos para esto')


def freakout(update: Update, context: CallbackContext):
    """Envía un gif de pánico."""
    try:
        context.bot.deleteMessage(chat_id=update.message.chat_id, message_id=update.message.message_id)
        context.bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.UPLOAD_PHOTO, timeout=10)
        context.bot.send_document(chat_id=update.message.chat_id, document=open('./gifs/freakout.mp4', 'rb'))
    except Exception:
        context.bot.send_message(chat_id=update.effective_chat.id, text='No tengo permisos para esto')


def mimos(update: Update, context: CallbackContext):  # TODO conseguir que responda al respondido por la orden
    """Envía un gif al azar de mimos."""
    try:
        context.bot.deleteMessage(chat_id=update.message.chat_id, message_id=update.message.message_id)
        context.bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.UPLOAD_PHOTO, timeout=10)
        directory = './gifs/mimos/'
        mimo = choice(os.listdir(directory))
        context.bot.send_document(chat_id=update.message.chat_id, document=open(directory + mimo, 'rb'))
    except Exception:
        context.bot.send_message(chat_id=update.effective_chat.id, text='No tengo permisos para esto')


def dakka(update: Update, context: CallbackContext):
    """Envía un gif al azar de mimos."""
    try:
        context.bot.deleteMessage(chat_id=update.message.chat_id, message_id=update.message.message_id)
        context.bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.UPLOAD_PHOTO, timeout=10)
        directory = './gifs/dakka/'
        gun = choice(os.listdir(directory))
        context.bot.send_document(chat_id=update.message.chat_id, document=open(directory + gun, 'rb'))
    except Exception:
        context.bot.send_message(chat_id=update.effective_chat.id, text='No tengo permisos para esto')


def mimimi(update: Update, context: CallbackContext):  # TODO conseguir que responda al respondido por la orden
    """Envía un gif de mimimi."""
    try:
        context.bot.deleteMessage(chat_id=update.message.chat_id, message_id=update.message.message_id)
        context.bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.UPLOAD_PHOTO, timeout=10)
        context.bot.send_document(chat_id=update.message.chat_id, document=open('./gifs/mimimi.mp4', 'rb'))
    except Exception:
        context.bot.send_message(chat_id=update.effective_chat.id, text='No tengo permisos para esto')
