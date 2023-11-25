from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from PIL import Image
import numpy as np

# Variables de la cámara
camera_distance = 5.0
camera_rotation = [0.0, 0.0]
camera_position = [0.0, 0.0]

# Variables para controlar la posición y la rotación de la mesa
table_x = 0.0
table_y = -0.45
table_z = 0.0
table_angle = 0.0

# Variables para el movimiento en el cuarto
room_x = 0.0
room_z = 0.0

# Variables para las sillas
chair_positions = [
    (1.0, -0.45, 1.0),
    (1.0, -0.45, -1.0),
    (-1.0, -0.45, 1.0),
    (-1.0, -0.45, -1.0)
]

# Variables para el control del mouse
mouse_down = False
last_x, last_y = 0, 0

# Variables para la lámpara
lamp_position = [0.0, 0.7, 0.0]  # Posición de la lámpara (encima de la mesa)
lamp_direction = [0.0, -1.0, 0.0]  # Dirección de la lámpara (hacia abajo)
lamp_color = [0.0, 0.0, 0.0, 1.0]  # Color de la lámpara (negro)
lamp_intensity = 3.0  # Intensidad de la lámpara (aumentada)

# Variable para controlar el estado de la lámpara
lamp_on = False  # Inicialmente, la lámpara está apagada

# Variable para controlar si el mouse hizo clic en la lámpara
lamp_clicked = False

# Variables para las texturas
floor_texture = None
wall_texture = None

def load_texture(image_path):
    image = Image.open(image_path)
    img_data = np.array(list(image.getdata()), np.uint8)
    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, image.width, image.height, 0, GL_RGB, GL_UNSIGNED_BYTE, img_data)
    return texture_id

def init_textures():
    global floor_texture, wall_texture
    floor_texture = load_texture("floor_texture.jpg")  # Reemplaza con la ruta a tu textura de piso
    wall_texture = load_texture("wall_texture.jpg")    # Reemplaza con la ruta a tu textura de pared

def draw_table():
    glPushMatrix()
    glTranslatef(table_x, table_y, table_z)
    glRotatef(table_angle, 0, 1, 0)
    glScalef(1.0, 0.1, 0.5)
    glColor3f(0.5, 0.25, 0.0)
    glutSolidCube(1.0)
    glPopMatrix()

    # Patas de la mesa
    for dx, dz in [(0.4, 0.4), (-0.4, 0.4), (0.4, -0.4), (-0.4, -0.4)]:
        glPushMatrix()
        glTranslatef(table_x + dx, table_y - 0.25, table_z + dz)
        glScalef(0.1, 0.5, 0.1)
        glColor3f(0.5, 0.25, 0.0)
        glutSolidCube(1.0)
        glPopMatrix()

def draw_chair(x, y, z):
    glPushMatrix()
    glTranslatef(x, y, z)
    glScalef(0.15, 0.1, 0.15)
    glColor3f(0.5, 0.25, 0.0)
    glutSolidCube(1.0)
    glPopMatrix()

    # Patas de la silla
    for dx, dz in [(0.07, 0.07), (-0.07, 0.07), (0.07, -0.07), (-0.07, -0.07)]:
        glPushMatrix()
        glTranslatef(x + dx, y - 0.25, z + dz)
        glScalef(0.03, 0.4, 0.03)
        glColor3f(0.5, 0.25, 0.0)
        glutSolidCube(1.0)
        glPopMatrix()

def draw_lamp():
    # Configuración de la lámpara
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, lamp_position)
    glLightfv(GL_LIGHT0, GL_SPOT_DIRECTION, lamp_direction)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, lamp_color)
    glLightf(GL_LIGHT0, GL_SPOT_CUTOFF, 30.0)  # Ángulo de apertura del spotlight

    # Intensidad de la lámpara
    if lamp_on:
        glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, lamp_intensity)
        glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)
    else:
        glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.0)
        glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.0)

    # Dibujo de la lámpara
    glPushMatrix()
    glTranslatef(lamp_position[0], lamp_position[1], lamp_position[2])
    glColor3f(lamp_color[0], lamp_color[1], lamp_color[2])
    glutSolidSphere(0.05, 20, 20)  # Puedes ajustar el tamaño y la calidad de la esfera
    glPopMatrix()


def draw_room():
    glBindTexture(GL_TEXTURE_2D, wall_texture)

    # Paredes color naranja
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0)
    glVertex3f(-2.0, -1.0, -2.0)
    glTexCoord2f(10, 0)
    glVertex3f(2.0, -1.0, -2.0)
    glTexCoord2f(10, 10)
    glVertex3f(2.0, 1.0, -2.0)
    glTexCoord2f(0, 10)
    glVertex3f(-2.0, 1.0, -2.0)

    glTexCoord2f(0, 0)
    glVertex3f(-2.0, -1.0, 2.0)
    glTexCoord2f(10, 0)
    glVertex3f(2.0, -1.0, 2.0)
    glTexCoord2f(10, 10)
    glVertex3f(2.0, 1.0, 2.0)
    glTexCoord2f(0, 10)
    glVertex3f(-2.0, 1.0, 2.0)

    # Eliminamos la pared del lado derecho
    glTexCoord2f(0, 0)
    glVertex3f(-2.0, -1.0, 2.0)
    glTexCoord2f(10, 0)
    glVertex3f(-2.0, -1.0, -2.0)
    glTexCoord2f(10, 10)
    glVertex3f(-2.0, 1.0, -2.0)
    glTexCoord2f(0, 10)
    glVertex3f(-2.0, 1.0, 2.0)
    glEnd()

    glBindTexture(GL_TEXTURE_2D, floor_texture)

    # Suelo en color amarillo
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0)
    glVertex3f(-2.0, -1.0, -2.0)
    glTexCoord2f(10, 0)
    glVertex3f(2.0, -1.0, -2.0)
    glTexCoord2f(10, 10)
    glVertex3f(2.0, -1.0, 2.0)
    glTexCoord2f(0, 10)
    glVertex3f(-2.0, -1.0, 2.0)
    glEnd()

    glBindTexture(GL_TEXTURE_2D, wall_texture)

    # Techo color blanco
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0)
    glVertex3f(-2.0, 1.0, -2.0)
    glTexCoord2f(10, 0)
    glVertex3f(2.0, 1.0, -2.0)
    glTexCoord2f(10, 10)
    glVertex3f(2.0, 1.0, 2.0)
    glTexCoord2f(0, 10)
    glVertex3f(-2.0, 1.0, 2.0)
    glEnd()

    glBindTexture(GL_TEXTURE_2D, wall_texture)

    # Puerta color rojo
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0)
    glVertex3f(-0.5, -1.0, 2.0)
    glTexCoord2f(1, 0)
    glVertex3f(0.5, -1.0, 2.0)
    glTexCoord2f(1, 1)
    glVertex3f(0.5, 0.5, 2.0)
    glTexCoord2f(0, 1)
    glVertex3f(-0.5, 0.5, 2.0)
    glEnd()

    glBindTexture(GL_TEXTURE_2D, wall_texture)

    # Ventana en la pared contraria a la puerta
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0)
    glVertex3f(2.0, 0.5, -0.1)
    glTexCoord2f(1, 0)
    glVertex3f(2.0, 0.5, 0.1)
    glTexCoord2f(1, 1)
    glVertex3f(2.0, 0.5, 0.1)
    glTexCoord2f(0, 1)
    glVertex3f(2.0, 0.5, -0.1)
    glEnd()


def toggle_lamp():
    global lamp_on
    lamp_on = not lamp_on
    glutPostRedisplay()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Configuración de la cámara
    glTranslatef(0.0, 0.0, -camera_distance)
    glRotatef(camera_rotation[0], 1, 0, 0)
    glRotatef(camera_rotation[1], 0, 1, 0)
    glTranslatef(-camera_position[0], -camera_position[1], 0.0)

    # Movimiento en el cuarto
    glTranslatef(room_x, 0.0, room_z)

    # Dibujo del cuarto
    draw_room()
    draw_table()
    for chair_pos in chair_positions:
        draw_chair(chair_pos[0], chair_pos[1], chair_pos[2])
    draw_lamp()  # Dibuja la lámpara

    glutSwapBuffers()

def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, (width / height), 1, 10)
    glMatrixMode(GL_MODELVIEW)

def special(key, x, y):
    global table_x, table_y, room_x, room_z

    if key == GLUT_KEY_LEFT:
        table_x -= 0.1
    elif key == GLUT_KEY_RIGHT:
        table_x += 0.1
    elif key == GLUT_KEY_UP:
        table_y += 0.1
    elif key == GLUT_KEY_DOWN:
        table_y -= 0.1

    # Movimiento en el cuarto
    if key == GLUT_KEY_LEFT:
        room_x -= 0.1
    elif key == GLUT_KEY_RIGHT:
        room_x += 0.1
    elif key == GLUT_KEY_UP:
        room_z -= 0.1
    elif key == GLUT_KEY_DOWN:
        room_z += 0.1

    glutPostRedisplay()

def mouse(button, state, x, y):
    global camera_position, camera_rotation, mouse_down, lamp_clicked

    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        camera_position = [x, y]
        mouse_down = True
        # Verificar si se hizo clic en la lámpara
        viewport = glGetIntegerv(GL_VIEWPORT)
        lamp_screen_pos = gluProject(lamp_position[0], lamp_position[1], lamp_position[2], glGetDoublev(GL_MODELVIEW_MATRIX), glGetDoublev(GL_PROJECTION_MATRIX), viewport)
        lamp_clicked = abs(lamp_screen_pos[0] - x) < 20 and abs(lamp_screen_pos[1] - (viewport[3] - y)) < 20
    elif button == GLUT_LEFT_BUTTON and state == GLUT_UP:
        camera_position = [0, 0]
        mouse_down = False
        lamp_clicked = False

def motion(x, y):
    global camera_position, camera_rotation, mouse_down

    if mouse_down:
        delta_x = x - camera_position[0]
        delta_y = y - camera_position[1]

        camera_rotation[1] += delta_x * 0.5
        camera_rotation[0] += delta_y * 0.5

        camera_position = [x, y]
        glutPostRedisplay()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow("Escenario 3D en PyOpenGL")

    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutSpecialFunc(special)
    glutMouseFunc(mouse)
    glutMotionFunc(motion)
    glEnable(GL_DEPTH_TEST)

    init_textures()  # Inicializa las texturas

    glutMainLoop()

if __name__ == "__main__":
    main()
