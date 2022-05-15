import datetime
from random import randint, sample
from telegram import Update, ChatAction
from telegram.ext import CallbackContext
from datos import characters, ban_chat_permissions, un_ban_chat_permissions


def serio(update: Update, context: CallbackContext) -> None:
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
        context.bot.send_message(chat_id=update.effective_chat.id, text="Nop, no puedo hacer eso")


def kill(update: Update, context: CallbackContext):
    """Juega a la ruleta rusa"""
    try:
        user = update.effective_user
        context.bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING, timeout=10)
        time = datetime.datetime.now()
        context.bot.restrictChatMember(chat_id=update.message.chat_id, user_id=user.id, until_date=time,
                                       permissions=ban_chat_permissions)
        context.bot.send_message(chat_id=update.effective_chat.id, text="Se hizo la automorición!")
    except Exception:
        context.bot.send_message(chat_id=update.effective_chat.id, text='Ojalá poder hacerlo, pero no tengo permiso...')


def angryupvote(update: Update, context: CallbackContext):
    try:
        user = update.effective_user
        context.bot.deleteMessage(chat_id=update.message.chat_id, message_id=update.message.message_id)
        context.bot.send_message(chat_id=update.effective_chat.id, parse_mode='MarkdownV2',
                                 text=f"A {user.mention_markdown_v2()} le gusta, pero no debería")
    except Exception:
        context.bot.send_message(chat_id=update.effective_chat.id, text='Ojalá poder hacerlo, pero no tengo permiso...')


def password(update: Update, context: CallbackContext):
    """Crea una contraseña de manera básica"""
    try:
        length = int(update.message.text.replace('/password', '').replace('@YOUR_BOT', ''))
        context.bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING, timeout=10)
        if length <= 0:
            update.message.reply_text(text='Me tomas por tonto?')
        elif length <= 50:
            temp = sample(characters, length)
            pword = "".join(temp)
            context.bot.send_message(chat_id=update.effective_chat.id, parse_mode='MarkdownV2',
                                     text=f"La longitud es {length} y la contraseña es:\n`{pword}`")
        else:
            update.message.reply_text(text='WOW! Algo que compensar?')
    except ValueError:
        context.bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING, timeout=10)
        update.message.reply_text(text='Necesito un puto número entero, no esta tontería')
