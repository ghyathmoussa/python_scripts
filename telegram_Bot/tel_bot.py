API_KEY = '5415277852:AAHCJj5fbXBmBOeRot_gFkq1BH3OLU3gYjc'

from datetime import datetime

def response_(in_text):
    user_msg = str(in_text).lower()

    if in_text in ['hello','hi','sup']:
        return 'Hi!, how can I help you!!'
    
    if in_text in ['who are you','can ypu help me']:
        return 'I am bot, how can I help you? press start/'
    
    if in_text in ['tiem','time?','date?']:
        new = datetime.now()
        dat_time = new.strtime('%d/%m/%y, %H:%M:%S')

        return dat_time
    
    return 'Please write a human sentences!!'

from telegram.ext import *

# commands functions

def start_command(update,context):
    update.message.replay_text('Starting now...')

def help_command(update,context):
    update.message.replay_text('Please type help/')

def handle_message(update,context):
    text = str(update.message.text).lower()

    response = response_(text)

    update.message.replay_text(response)

def handle_error(update,context):
    print(f'update: {update}')

def main():
    updater = Updater(API_KEY,use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start',start_command))

    dp.add_handler(CommandHandler('help',help_command))
    
    dp.add_handler(MessageHandler(Filters.text,handle_message))

    dp.add_error_handler(handle_error)

    updater.start_polling(3)

    updater.idle()

main()