from telegram.ext import *
    


TOKEN = '6505554156:AAHQbeY41GEUrc6vrJ3jtdvnVb-TAVgAT14'

print('Starting a bot.... c==3')
     
async def dziadek_command(update, context):
    await update.message.reply_text('DZIADEK WIEDZIAL, NIE POWIEDZIAL...')

async def print_menu_command(update, context):
    await update.message.reply_text('   Hello Welcome to Store   \n option1 -> /option1command \n option2 -> /option2command')

async def print_store_command(update, context):
    await update.message.reply_text('- AK 47 (Sativa)\n -Lemon Haze (Sativa) \n -Amnesia Haze (Indica)')


#Pomidor13

if __name__ == '__main__':
    application = Application.builder().token(TOKEN).build()

    # Commands
    application.add_handler(CommandHandler('start', dziadek_command))

    application.add_handler(CommandHandler('menu', print_menu_command))

    application.add_handler(CommandHandler('store', print_store_command))

    # Run bot
    application.run_polling(1.0)