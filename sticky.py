import time
from random import choice
from telegram import ChatAction, Update
from telegram.ext import CallbackContext
from datos import love_list


def love(update: Update, context: CallbackContext):
    loving = choice(love_list)
    context.bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.CHOOSE_STICKER, timeout=20)
    time.sleep(2)
    context.bot.send_sticker(chat_id=update.effective_chat.id, sticker=loving)
