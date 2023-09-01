import pygame
import sys

# Inicializar Pygame y el módulo de joystick
pygame.init()
pygame.joystick.init()

# Verificar si hay joysticks disponibles
if pygame.joystick.get_count() == 0:
    print("No se encontraron joysticks.")
    pygame.quit()
    sys.exit()

# Inicializar el primer joystick
joystick = pygame.joystick.Joystick(0)
joystick.init()

# Configurar la ventana Pygame
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Joystick Example")

# Bucle principal
running = True

# Variables para almacenar los valores anteriores
prev_axes = [0.0] * joystick.get_numaxes()
prev_buttons = [0] * joystick.get_numbuttons()
prev_state = None

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Leer los valores del joystick
    axes = [joystick.get_axis(i) for i in range(joystick.get_numaxes())]
    buttons = [joystick.get_button(i) for i in range(joystick.get_numbuttons())]

    current_state = (axes, buttons)

    if current_state != prev_state:
        print("Ejes:", axes)
        print("Botones:", buttons)
        print("----------------------")
        prev_state = current_state

    screen.fill((0, 0, 0))  # Limpiar la pantalla
    pygame.display.flip()
"""    if axes != prev_axes or buttons != prev_buttons:
        print("Ejes:", axes)
        print("Botones:", buttons)
        print("----------------------")
        prev_axes = list(axes)
        prev_buttons = list(buttons)"""



# Finalizar Pygame
pygame.quit()
sys.exit()