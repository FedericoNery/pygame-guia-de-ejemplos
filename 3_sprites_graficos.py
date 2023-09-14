import pygame

pygame.init()

# Configuración de la ventana
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Mi Juego")

# Cargar imagen
player_image = pygame.image.load("bulbasaur.png")

# Crear sprite
player = pygame.Rect(100, 100, player_image.get_width(), player_image.get_height())
player_color = (255, 0, 0)  # Color del borde (rojo en formato RGB)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("Espacio presionado")

    # Dibujar el borde del rectángulo
    pygame.draw.rect(window, player_color, player, 2)  # El último argumento (2) es el grosor del borde

    # Renderizar sprite (imagen) dentro del rectángulo
    window.blit(player_image, player)

    pygame.display.update()

pygame.quit()
