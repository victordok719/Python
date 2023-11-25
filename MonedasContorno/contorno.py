import cv2

imagen = cv2.imread('contorno.jpg')
grises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
umbral = cv2.threshold(grises,100,255,cv2.THRESH_BINARY)





#Mostrar
cv2.imshow('imagen',imagen) #mostamos la imagen
cv2.imshow('imagen en grises',grises)
cv2.imshow('umbral',umbral[1])
cv2.waitKey(0) #Indicamos a python que no cierre inmediatamente la imagen
#Con valor 1 funciona para el reconocimiento facial o mostrar algun video
#COn un valor de 0 se vuelve estatico
cv2.destroyAllWindows() #Destruye todas las ventanas abiertas

