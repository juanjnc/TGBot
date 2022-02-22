import logging

from telegram.ext import CommandHandler, MessageHandler, Filters, Updater

import control
import gifs
import otters
import pics
import rpg_array
import rpg_pj
import rpg_others
import spam
import sticky

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    updater = Updater(token='YOUR_TOKEN', use_context=True)  # TODO YOUR_TOKEN
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', control.start))
    dispatcher.add_handler(CommandHandler('github', spam.github))
    dispatcher.add_handler(CommandHandler('rpgdr', spam.descargar))
    dispatcher.add_handler(CommandHandler('osr', rpg_array.osr))
    dispatcher.add_handler(CommandHandler('d20', rpg_array.d20))
    dispatcher.add_handler(CommandHandler('microlite3d6', rpg_array.microlite3d6))
    dispatcher.add_handler(CommandHandler('microlite4d6', rpg_array.microlite4d6))
    dispatcher.add_handler(CommandHandler('coc6', rpg_array.coc))
    dispatcher.add_handler(CommandHandler('coc7', rpg_array.coc7))
    dispatcher.add_handler(CommandHandler('pjerdd', rpg_pj.pjerdd))
    dispatcher.add_handler(CommandHandler('pj13thage', rpg_pj.pj13thage))
    dispatcher.add_handler(CommandHandler('roll', rpg_others.roll))
    dispatcher.add_handler(CommandHandler('jdr', rpg_others.recomendar_rpg))
    dispatcher.add_handler(CommandHandler('crisu', gifs.pug))
    dispatcher.add_handler(CommandHandler('nada', gifs.nada))
    dispatcher.add_handler(CommandHandler('freakout', gifs.freakout))
    dispatcher.add_handler(CommandHandler('dance', gifs.dance))
    dispatcher.add_handler(CommandHandler('mimos', gifs.mimos))
    dispatcher.add_handler(CommandHandler('dakka', gifs.dakka))
    dispatcher.add_handler(CommandHandler('mimimi', gifs.mimimi))
    dispatcher.add_handler(CommandHandler('s', otters.serio))
    dispatcher.add_handler(CommandHandler('angryupvote', otters.angryupvote))
    dispatcher.add_handler(CommandHandler('noc', pics.nocombat))
    dispatcher.add_handler(CommandHandler('noh', pics.nohorny))
    dispatcher.add_handler(CommandHandler('ruleta', otters.rusa))
    dispatcher.add_handler(CommandHandler('kill', otters.kill))
    dispatcher.add_handler(CommandHandler('love', sticky.love))
    # Siempre al final
    dispatcher.add_handler(MessageHandler(Filters.command, control.unknown))

    updater.start_polling()
    # Block until you press Ctrl-C or the process receives SIGINT, SIGTERM or
    # SIGABRT. This should be used most of the time, since start_polling() is
    # non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
