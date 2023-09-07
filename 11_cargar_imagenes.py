import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
ventana_ancho = 800
ventana_alto = 400
ventana = pygame.display.set_mode((ventana_ancho, ventana_alto))
pygame.display.set_caption("Ejemplo de carga de imágenes de cartas de póker")

# Cargar imágenes de cartas
carta_1 = pygame.image.load("cardBack_blue1.png")  # Reemplaza "cardBack_blue1.png" con el nombre de tu archivo de imagen
carta_2 = pygame.image.load("cardDiamonds2.png")  # Reemplaza "cardDiamonds2.png" con el nombre de tu archivo de imagen

# Escalar las imágenes de las cartas para que se ajusten a la ventana
carta_1 = pygame.transform.scale(carta_1, (100, 150))
carta_2 = pygame.transform.scale(carta_2, (100, 150))

# Posiciones de las cartas
posicion_carta_1 = (100, 150)
posicion_carta_2 = (300, 150)

# Loop principal del juego
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Llenar la ventana con color blanco
    ventana.fill((0,100,0))

    # Dibujar las cartas en la ventana
    ventana.blit(carta_1, posicion_carta_1)
    ventana.blit(carta_2, posicion_carta_2)

    # Actualizar la pantalla
    pygame.display.update()
