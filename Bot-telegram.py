from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import response as R
from telegram.ext.conversationhandler import ConversationHandler
import telegram

updater = Updater("5587176957:AAG-0Rl51NDeQ08DUTG0oq45aWORIZVFSNs",
				use_context=True)
# bot = telegram.Bot(token="5587176957:AAG-0Rl51NDeQ08DUTG0oq45aWORIZVFSNs")
# user_id = '21870'

# ---------- defining states ---------
ONE , TWO, THREE = range(3)

tracker = {
        'city': '',
        'credit' : '',
        'rent' : '',
    }

def start(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Hello sir, Welcome to the Bot.Please write\
		/help to see the commands available.")

def help(update: Update, context: CallbackContext):
	update.message.reply_text("""Available Commands :-
	/Track_Rent - To Track Rent ...
	""")


def Track_Rent(update: Update, context: CallbackContext):
    # chat_id = update.message.chat_id
    update.message.reply_text("hello , you are registering ! please enter your city")
    return ONE

def got_city(update: Update, context: CallbackContext):
    # chat_id = update.message.chat_id
    city = update.message.text # now we got the name
    if city == 'cancel':
        cancel(update, context)
        return ConversationHandler.END
    context.user_data["city"] = city # to use it later (in next func)
    update.message.reply_text(f"thanks ,your city is: {city} ! please enter your credit value")
    return TWO


def got_credit(update: Update, context: CallbackContext):
    # chat_id = update.message.chat_id
    credit = update.message.text # now we got the name
    city = context.user_data["city"]
    context.user_data["credit"] = credit # to use it later (in next func)
    update.message.reply_text(f"{city},thanks your credit is : {credit} ! please enter your rent value")
    return THREE

def got_rent(update: Update, context: CallbackContext):
    # chat_id = update.message.chat_id
    rent = update.message.text # now we got the phone number
    context.user_data["rent"] = rent # we had the name , remember ?!
    city = context.user_data["city"]
    credit = context.user_data["credit"]
    update.message.reply_text(f"completed ! your city is {city} , your credit is {credit} and your rent is {rent}")
    return ConversationHandler.END

def cancel(update: Update, context: CallbackContext):
    #  chat_id = update.message.chat_id
     update.message.reply_text("process canceled !")
     return ConversationHandler.END

def unknown_text(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Sorry I can't recognize you , you said '%s'" % update.message.text)

def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry '%s' is not a valid command" % update.message.text)

# ---------- conversation handler ---------
CH = ConversationHandler (entry_points = [CommandHandler("Track_Rent", Track_Rent)],
     states = {
        ONE : [MessageHandler(Filters.text , got_city)],
        TWO : [MessageHandler(Filters.text , got_credit)],
        THREE: [MessageHandler(Filters.text , got_rent)]
     },
     fallbacks = [MessageHandler(Filters.text('cancel'), cancel)],
     allow_reentry = True)

updater.dispatcher.add_handler(CH)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
# updater.dispatcher.add_handler(CommandHandler('Track_Rent', Track_Rent))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(
    # Filters out unknown commands
    Filters.command, unknown))
  
# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()
