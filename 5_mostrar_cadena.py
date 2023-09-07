import pygame

pygame.init()

# Configuración de la ventana
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Mi Juego")

score = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("Espacio presionado")

    # Mostrar puntuación
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Puntuación: {score}", True, (255, 255, 255))
    window.blit(score_text, (10, 10))

    pygame.display.update()

pygame.quit()
