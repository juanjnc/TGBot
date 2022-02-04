from telegram import ChatAction, Update
from telegram.ext import CallbackContext


def github(update: Update, context: CallbackContext):
    """Envía info de Github."""
    context.bot.deleteMessage(chat_id=update.message.chat_id, message_id=update.message.message_id)
    context.bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING, timeout=10)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Hola, este es el GitHub del autor\nhttps://github.com/juanjnc/')


def descargar(update: Update, context: CallbackContext):
    """Envía info de RPGDR."""
    context.bot.deleteMessage(chat_id=update.message.chat_id, message_id=update.message.message_id)
    context.bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING, timeout=10)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Desde aquí puedes descargar la última versión de RPGDiceRoller'
                                  '\nhttps://github.com/juanjnc/RPGDiceRoller/releases')
