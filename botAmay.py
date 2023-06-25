#done by AMAY BAHAR WAYKOOL

# My token ==> 5934248911:AAH7-EcXFZA_dX6C0dWjd9GDvzM835quutY

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def start_bot(update,context):
    # Your bot will send this message when users first talk to bot 
    #using /start command
    update.message.reply_text('Hi! Welcome. Please give me any text and i will echo it for you')

def need_help(update, context):     
   # on /help command
   update.message.reply_text('Help!')


def echo(update, context):     
   update.message.reply_text(f"{update.message.text} Amay W.)


def main():
    updater = Updater('5934248911:AAH7-EcXFZA_dX6C0dWjd9GDvzM835quutY')
    dp = updater.dispatcher    
    dp.add_handler(CommandHandler('start',start_bot))
    dp.add_handler(CommandHandler('help',need_help))      
    dp.add_handler(MessageHandler(Filters.text, echo))
    updater.start_polling()
    updater.idle()


                            
