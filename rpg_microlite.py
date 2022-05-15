""" generates random monster for Microlite20. Adapted from 1d4chan"""
from random import randint, choice
from math import floor
from re import compile, search
from telegram import Update, ChatAction
from telegram.ext import CallbackContext

np = {
    'W': 'CT CT CX CDF CVFT CDFU CTU IT ICT A',
    'A': 'KVKVtion',
    'K': 'b c d f g j l m n p qu r s t v sP',
    'I': 'ex in un re de',
    'T': 'VF VEe',
    'U': 'er ish ly en ing ness ment able ive',
    'C': 'b c ch d f g h j k l m n p qu r s sh t th v w y sP Rr Ll',
    'E': 'b c ch d f g dg l m n p r s t th v z',
    'F': 'b tch d ff g gh ck ll m n n ng p r ss sh t tt th x y zz rR sP lL',
    'P': 'p t k c',
    'Q': 'b d g',
    'L': 'b f k p s',
    'R': 'P Q f th sh',
    'V': 'a e i o u',
    'D': 'aw ei ow ou ie ea ai oy',
    'X': 'e i o aw ow oy'
}

atktypes = 'Bite Claw Slam Gore Sting Tentacle Shock Broadsword Battleaxe Club Glaive Spear Falchion Dagger'




def new_word():
    # Generates a random name with some clever regex golf
    word = 'W'
    p = compile('[A-Z]')
    while len(word) < 40:
        match = search(p, word)
        if match:
            matched = match.group(0)
        else:
            return word.capitalize()
        word = word.replace(matched, choice(np[matched].split(' ')))
    return word.capitalize()


def micro_monster(hd):
    # Generates stats and formats output
    construct = f"Name: {new_word()}\n"
    construct += f"HD: {hd} \({int(floor(hd * 4.5)) + randint(0, hd * 4)}hp\), "
    construct += f"AC: {randint(0, 5) + hd + 10}, "
    construct += f"Attack: {choice(atktypes.split(' '))} \+ { hd + randint(0, 4)} "
    construct += f"\({randint(0, 2) + 1}d{2 * (randint(0, 6) + 1)}\)'\n"
    # print(construct)
    return construct


'''hd = int(input("Enter number of hit dice(whole number): "))
micro_monster(hd)'''


def bestiary_microlite(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    try:
        hd = int(update.message.text.replace('/micromonster', '').replace('@YOUR_BOT', ''))
        if hd > 0:
            monster = micro_monster(hd=hd)
            context.bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING, timeout=15)
            update.message.reply_text(text=f'Tu monstruo con HD *{hd}* es:\n\n_{monster}_',
                                      parse_mode='MarkdownV2')
        else:
            context.bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING, timeout=10)
            update.message.reply_markdown_v2(f'{user.mention_markdown_v2()} esos números son un poco peregrinos\.\.\.')

    except ValueError:
        context.bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING, timeout=10)
        update.message.reply_markdown_v2(f'{user.mention_markdown_v2()} ¿Tan difícil es poner un número\?')

