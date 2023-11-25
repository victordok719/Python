import cv2
import dlib

# Inicializar el detector de caras de dlib
detector = dlib.get_frontal_face_detector()

# Cargar el modelo de detección de puntos faciales de dlib (shape predictor)
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

# Inicializar la cámara
cap = cv2.VideoCapture(0)

while True:
    # Leer el cuadro de video
    ret, frame = cap.read()

    # Convertir el cuadro a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar caras en el cuadro
    faces = detector(gray)

    # Iterar sobre las caras detectadas
    for face in faces:
        # Obtener los puntos faciales
        landmarks = predictor(gray, face)

        # Iterar sobre los puntos faciales y dibujarlos en el cuadro
        for n in range(0, 68):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)

    # Mostrar el cuadro resultante
    cv2.imshow('Facial Landmarks', frame)

    # Salir si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar los recursos
cap.release()
cv2.destroyAllWindows()
