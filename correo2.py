import smtplib

#datos
username=input("pon tu correo:")
password=input("introduce tu contraseña:")
destinatario=input("correo de destino:")
msg=input("escribe el texto del mensaje:")

#enviando el correo
server=smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(remitente,destinatario,msg)
server.quit()