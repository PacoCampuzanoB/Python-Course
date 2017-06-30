import telebot #importamos el modulo	
TOKEN = '324734708:AAHtl3dSdx-2jw-_QVnu3DIaaFBFR4msacE'	#llave de mi bot
miBot = telebot.TeleBot(TOKEN)	#Instancia del bot

def listener(mensajes):	
	for m in mensajes:
		chat_id = m.chat.id 	#regresa el id del que mande mensajes
		if m.content_type == 'text':  #verificamos que el mensaje sea de tipo texto
			text =m.text 		#Guardar ese texto
			#miBot.send_message(chat_id,"Soy un loro, soy un loroBot!") ##Mensaje
			miBot.send_message(chat_id,"Soy un loro Spam!!!")
			while True:
				miBot.send_message(chat_id,"Spameado por mandar mensaje")
			miBot.send_message(chat_id,text) #Pasamos el texto obtenido al chat

miBot.set_update_listener(listener) #Cambiamos la funcion de cuando recibe un mensaje
miBot.polling()	#Actualizamos