import pygame
import random

# Inicialización del juego
pygame.init()

# Dimensiones de la ventana del juego
ancho_ventana = 640
alto_ventana = 480

# Colores RGB
color_negro = (0, 0, 0)
color_verde = (0, 255, 0)
color_rojo = (255, 0, 0)
color_blanco = (255, 255, 255)

# Tamaño de cada segmento de la serpiente y velocidad del juego
tamaño_segmento = 20
velocidad = 10

# Crear la ventana del juego
ventana = pygame.display.set_mode((ancho_ventana, alto_ventana))
pygame.display.set_caption('Juego de la Serpiente')

# Reloj para controlar la velocidad del juego
reloj = pygame.time.Clock()

# Fuente para el puntaje
fuente = pygame.font.SysFont(None, 30)

# Función para mostrar el puntaje en la ventana
def mostrar_puntaje(puntaje):
    texto_puntaje = fuente.render("Puntaje: " + str(puntaje), True, color_blanco)
    ventana.blit(texto_puntaje, (10, 10))

# Función para mostrar un mensaje en la ventana
def mostrar_mensaje(mensaje, color):
    texto = fuente.render(mensaje, True, color)
    ventana.blit(texto, (ancho_ventana // 2 - texto.get_width() // 2, alto_ventana // 2 - texto.get_height() // 2))
    pygame.display.update()

# Bucle principal del juego
def juego_serpiente():
    juego_terminado = False
    fin_juego = False

    # Posición inicial de la serpiente
    x = ancho_ventana // 2
    y = alto_ventana // 2

    # Velocidad inicial de la serpiente
    cambio_x = 0
    cambio_y = 0

    # Posición inicial de la comida
    comida_x = round(random.randrange(0, ancho_ventana - tamaño_segmento) / 20.0) * 20.0
    comida_y = round(random.randrange(0, alto_ventana - tamaño_segmento) / 20.0) * 20.0

    # Segmentos de la serpiente
    segmentos = []

    # Longitud inicial de la serpiente
    longitud = 1

    # Puntaje inicial
    puntaje = 0

    while not juego_terminado:
        while fin_juego:
            ventana.fill(color_negro)
            mostrar_mensaje("Juego terminado. Presiona R para reiniciar o Q para salir.", color_rojo)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        juego_serpiente()
                    elif event.key == pygame.K_q:
                        juego_terminado = True
                        fin_juego = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                juego_terminado = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and cambio_x != tamaño_segmento:
                    cambio_x = -tamaño_segmento
                    cambio_y = 0
                elif event.key == pygame.K_RIGHT and cambio_x != -tamaño_segmento:
                    cambio_x = tamaño_segmento
                    cambio_y = 0
                elif event.key == pygame.K_UP and cambio_y != tamaño_segmento:
                    cambio_y = -tamaño_segmento
                    cambio_x = 0
                elif event.key == pygame.K_DOWN and cambio_y != -tamaño_segmento:
                    cambio_y = tamaño_segmento
                    cambio_x = 0

        if x >= ancho_ventana or x < 0 or y >= alto_ventana or y < 0:
            fin_juego = True

        x += cambio_x
        y += cambio_y

        ventana.fill(color_negro)
        pygame.draw.rect(ventana, color_verde, [comida_x, comida_y, tamaño_segmento, tamaño_segmento])

        cabeza = []
        cabeza.append(x)
        cabeza.append(y)
        segmentos.append(cabeza)

        if len(segmentos) > longitud:
            del segmentos[0]

        for segmento in segmentos[:-1]:
            if segmento == cabeza:
                fin_juego = True

        for segmento in segmentos:
            pygame.draw.rect(ventana, color_verde, [segmento[0], segmento[1], tamaño_segmento, tamaño_segmento])

        mostrar_puntaje(puntaje)

        pygame.display.update()

        if x == comida_x and y == comida_y:
            comida_x = round(random.randrange(0, ancho_ventana - tamaño_segmento) / 20.0) * 20.0
            comida_y = round(random.randrange(0, alto_ventana - tamaño_segmento) / 20.0) * 20.0
            longitud += 1
            puntaje += 1

        reloj.tick(velocidad)

    pygame.quit()

# Iniciar el juego
juego_serpiente()
