from telegram.ext import *

import response as R

updater = Updater("5587176957:AAG-0Rl51NDeQ08DUTG0oq45aWORIZVFSNs")

def handle_messages(update,context):

    text = str(update.message.text)

    response = R.sample_responses(text)

    update.message.reply_text(response)


d = updater.dispatcher

d.add_handler(MessageHandler(Filters.text, handle_messages))

updater.start_polling()

updater.idle()

