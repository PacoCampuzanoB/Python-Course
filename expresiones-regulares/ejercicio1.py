# validar correo electronico
# [a-z] 
# [A-Z]
# [0-9]
# [._-]
# @
# [a-z]
# [A-Z]
# [.-]

# hola@hotmail.com
# hola@alejandrozepeda.mx
# nombre@me.com.mx
# jorge123-banuelos@gmail.tk
# jorge_banuelos_123@al-go.com.mx
# pedronoe@comunidad.unam.mx
# jorge.banuelos@gmail.com
# alejandro@asdas.com.mx

# a@a
# alex@.com
# 0@@0.com
# .@gmail.com

import re
correo = input("Ingresa un correo: ")
expresion = "^[\w\d]+[\w\d.-]*@{1}\w+\.[a-z]{2,5}\.?[a-z]{2,5}?$"
if re.match(expresion, correo):
	print("Correo valido")
else:
	print("Correo invalido")

#[\w\d]+[\w\d.-]*@{1}\w+\.[a-z]{2,5}(\.[a-z]{2,5})?$