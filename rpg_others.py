import time
from random import choice, randint
from telegram import Update, ChatAction
from telegram.ext import CallbackContext
from datos import rpg_list


def roll(update: Update, context: CallbackContext):
    """Lanza dados usando el formato XdY."""
    user = update.effective_user
    try:
        die = update.message.text.replace('/roll', '').replace('@YOURBOT', '').lower().split('d')  # TODO @YOURBOT
        quantity, faces = int(die[0]), int(die[1])
        context.bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING, timeout=20)
        time.sleep(3)
        result = []
        if (1 < faces < 101) and (0 < quantity < 101):
            for i in range(quantity):
                rolls = randint(1, faces)
                result.append(rolls)
            suma = sum(result)
            update.message.reply_text(text=f'Tu tirada ha sido de:\n_*{result}*_\nCon un valor total de: _*{suma}*_',
                                      parse_mode='MarkdownV2')
        else:
            update.message.reply_markdown_v2(f'{user.mention_markdown_v2()} ¿En que piensas con esos números\?')
    except ValueError:
        context.bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING, timeout=10)
        update.message.reply_markdown_v2(f'{user.mention_markdown_v2()} ¿Tan difícil es poner los dados que quieres\?')


def recomendar_rpg(update: Update, context: CallbackContext):
    """Recomienda un Juego de Rol al Azar"""
    rpg = choice(rpg_list)
    context.bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING, timeout=15)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=f"Hola, tengo muchos para recomendar, unos {len(rpg_list)}, déjame que piense...")
    time.sleep(2)
    context.bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING, timeout=30)
    time.sleep(5)
    if rpg == 'FATAL':
        update.message.reply_text(text=f'Prueba este juego, *_{rpg}_*, seguro que te encanta cuando lo juegues\.',
                                  parse_mode='MarkdownV2')
        time.sleep(2)
        context.bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING, timeout=5)
        context.bot.send_message(text='Por si no lo pilláis, va en coña...')
    else:
        update.message.reply_text(text=f'Prueba este juego, *_{rpg}_*, seguro que te encanta cuando lo juegues\.',
                                  parse_mode='MarkdownV2')