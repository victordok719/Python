#l/usr/bin/python
#-*- coding: utf-8 -*-

#Enviar correo Gmail con python

import smtplib

remitente = 'codigodata@gmail.com'
destinatario='carlosblancogomez69@gmail.com'
msg= 'Correo enviado utilizando Python + smtplib en www.codigodata.com'

#Datos
username='codigodata@fmail.com'
password='Dejer2341XXX22t'

#Enviando el  correo

server=smtplib.SMTP('smtp.gmail.com:587')  #
server.starttls()  #inicia conexion
server.login(username,password)
server.sendmail(remitente,destinatario,msg)
server.quit()