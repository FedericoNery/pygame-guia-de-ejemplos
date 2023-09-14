import pygame

pygame.init()

# Configuración de la ventana
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Mi Juego")

enemy_image =pygame.image.load("sprigatito.png")
enemy = pygame.Rect(300, 100, enemy_image.get_width(), enemy_image.get_height())

# Cargar imagen
player_image = pygame.image.load("bulbasaur.png")

# Crear sprite
player = pygame.Rect(100, 100, player_image.get_width(), player_image.get_height())

player_color = (255, 0, 0)
enemy_color = (0, 255, 0)

pygame.draw.rect(window, player_color, player, 2)
pygame.draw.rect(window, enemy_color, enemy, 2)

window.blit(player_image, player.topleft)
window.blit(enemy_image, enemy.topright)
pygame.display.update()

running = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("Espacio presionado")
            elif event.key == pygame.K_LEFT:
                enemy.x = enemy.x - 10
            elif event.key == pygame.K_RIGHT:
                enemy.x = enemy.x + 10
    window.fill((0, 0, 0))
    pygame.draw.rect(window, player_color, player, 2)
    pygame.draw.rect(window, enemy_color, enemy, 2)
    window.blit(player_image, player)
    window.blit(enemy_image, enemy)
    pygame.display.update()

    if player.colliderect(enemy):
        print("Colisión con enemigo")

pygame.quit()

