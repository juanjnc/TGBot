from telegram import Update, ChatAction
from telegram.ext import CallbackContext


def start(update: Update, context: CallbackContext):
    """Envía un mensaje cuando se manda el comando /start."""
    context.bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING, timeout=10)
    user = update.effective_user
    update.message.reply_markdown_v2(fr'Hola {user.mention_markdown_v2()}, encantado de conocerte\!')


def unknown(update: Update, context: CallbackContext):
    """Para comando no reconocido"""
    context.bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING, timeout=10)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Ente, no puedo hacer algo para no que no estoy programado. Háztelo mirar, gracias")
