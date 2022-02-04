import datetime
from random import randint
from telegram import Update, ChatAction, ChatPermissions
from telegram.ext import CallbackContext

ban_chat_permissions = ChatPermissions(
    can_send_messages=False,
    can_send_media_messages=False,
    can_send_other_messages=False,
    can_send_polls=False,
    can_add_web_page_previews=False,)

un_ban_chat_permissions = ChatPermissions(
    can_send_messages=True,
    can_send_media_messages=True,
    can_send_other_messages=True,
    can_send_polls=True,
    can_add_web_page_previews=True,)


def serio(update: Update, context: CallbackContext):
    """Indica que el comentario va a broma"""
    context.bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING, timeout=10)
    update.message.reply_text('Por si no lo pilláis, va en coña...')


def rusa(update: Update, context: CallbackContext):
    """Juega a la ruleta rusa"""
    user = update.effective_user
    tambor = randint(1, 6)
    context.bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING, timeout=10)
    time = datetime.datetime.now() - datetime.timedelta(minutes=50)
    try:
        if tambor == 1:
            context.bot.restrictChatMember(chat_id=update.message.chat_id, user_id=user.id, until_date=time,
                                           permissions=ban_chat_permissions)
            context.bot.send_message(chat_id=update.effective_chat.id, text="Bala!")
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text="Tuviste suerte...\nPor ahora...")

    except Exception:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Nop, tu mejor no")


def kill(update: Update, context: CallbackContext):
    """Juega a la ruleta rusa"""
    user = update.effective_user
    context.bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING, timeout=10)
    time = datetime.datetime.now()
    context.bot.restrictChatMember(chat_id=update.message.chat_id, user_id=user.id, until_date=time,
                                   permissions=ban_chat_permissions)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Se hizo la automorición!")
