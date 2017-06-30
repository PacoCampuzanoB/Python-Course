import telebot

def molestar():
	TOKEN = '324734708:AAHtl3dSdx-2jw-_QVnu3DIaaFBFR4msacE'
	miBot =  telebot.TeleBot(TOKEN)
	text ='Aqui Molestando :)'
	chat_id = 393212953
	while True:
		miBot.send_message(chat_id,text)

molestar()