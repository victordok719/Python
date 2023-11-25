import turtle
import tkinter

# Definir la función para dibujar un pétalo
def draw_petal(t, radius):
    t.circle(radius, 60)
    t.left(120)
    t.circle(radius, 60)
    t.left(120)

# Crear una ventana de dibujo
window = turtle.Screen()

# Crear una tortuga para dibujar
flower = turtle.Turtle()

# Cambiar el color de la tortuga a amarillo
flower.color("yellow")

# Configurar el ancho de la línea
flower.width(3)

# Dibujar los pétalos
petal_radius = 100
for i in range(40):
    draw_petal(flower, petal_radius)
    flower.left(10)

# Mover la tortuga al centro de la flor
flower.penup()
flower.goto(0, 0)
flower.pendown()

# Cambiar el color de la tortuga a marrón para dibujar el centro de la flor
flower.color("brown")

# Dibujar el centro de la flor
flower.dot(50)

# Ocultar la tortuga y cerrar la ventana de dibujo al hacer clic en ella
flower.hideturtle()
window.exitonclick()