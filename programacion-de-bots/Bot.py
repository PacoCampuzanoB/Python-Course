import telebot
TOKEN = '324734708:AAHtl3dSdx-2jw-_QVnu3DIaaFBFR4msacE'

miBot = telebot.TeleBot(TOKEN)

print(miBot.get_me())  #Informacion del Bot

mensaje = "Hola, soy unh bot"  #simple mensaje
chat_id = 393212953	#lo sacamos de userinfobot

miBot.send_message(chat_id,mensaje)

##Enviar imagenes
foto = open('Koala.jpg','rb') ##Foto en la misma o carpte o con toda la ruta C:\usuario\Imagenes\...
miBot.send_photo(chat_id,foto)  ##el numero de chat y la foto

##Enviar Documentos
doc = open('Bot.py','rb')
miBot.send_document(chat_id,doc)

##Enviar Audio
#audio = open('cancion.mp3','rb')
#miBot.send_audio(chat_id,audio)

##Enviar Videos
#video = open('video.mp4','rb')
#miBot.send_video(chat_id,video)

##Enviar Ubicacion
latitud = 19.331493
longitud = -99.185065
miBot.send_location(chat_id,latitud,longitud)

from telebot import types

markup = types.ReplyKeyboardMarkup(row_width=2)
item1 = types.KeyboardButton('hola')
item2 = types.KeyboardButton('adios')
item3 = types.KeyboardButton('c')
markup.add(item1,item2, item3)

miBot.send_message(chat_id,'Elige una letra',reply_markup=markup)
