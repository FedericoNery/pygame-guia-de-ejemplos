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
player = pygame.Rect(100, 100, 50, 50)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("Espacio presionado")

    # Renderizar sprite
    window.blit(player_image, player.topleft)
    pygame.display.update()

pygame.quit()
