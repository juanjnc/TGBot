from telegram import ChatAction, Update
from telegram.ext import CallbackContext


def github(update: Update, context: CallbackContext):
    """Envía info de Github."""
    try:
        context.bot.deleteMessage(chat_id=update.message.chat_id, message_id=update.message.message_id)
        context.bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING, timeout=10)
        context.bot.send_message(chat_id=update.effective_chat.id,
                                text='Hola, este es el GitHub de @JuanJNC\nhttps://github.com/juanjnc/')
    except Exception:
        context.bot.send_message(chat_id=update.effective_chat.id, text='No tengo permisos para esto')


def descargar(update: Update, context: CallbackContext):
    """Envía info de RPGDR."""
    try:
        context.bot.deleteMessage(chat_id=update.message.chat_id, message_id=update.message.message_id)
        context.bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING, timeout=10)
        context.bot.send_message(chat_id=update.effective_chat.id,
                                text='Desde aquí puedes descargar la última versión de RPGDiceRoller'
                                    '\nhttps://github.com/juanjnc/RPGDiceRoller/releases')
    except Exception:
        context.bot.send_message(chat_id=update.effective_chat.id, text='No tengo permisos para esto')
