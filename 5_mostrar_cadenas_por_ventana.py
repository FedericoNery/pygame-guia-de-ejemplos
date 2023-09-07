import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
ventana_ancho = 400
ventana_alto = 300
ventana = pygame.display.set_mode((ventana_ancho, ventana_alto))
pygame.display.set_caption("Ejemplo de Pygame")

# Definir colores
blanco = (255, 255, 255)
negro = (0, 0, 0)

# Fuente y tamaño de texto
fuente = pygame.font.Font(None, 36)

# Texto que deseas mostrar
texto = "Hola, Pygame!"

# Loop principal del juego
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Llenar la ventana con color blanco
    ventana.fill(blanco)

    # Crear un objeto de texto
    texto_objeto = fuente.render(texto, True, negro)

    # Obtener el rectángulo del objeto de texto
    texto_rect = texto_objeto.get_rect()

    # Centrar el texto en la ventana
    texto_rect.center = (ventana_ancho // 2, ventana_alto // 2)

    # Dibujar el texto en la ventana
    ventana.blit(texto_objeto, texto_rect)

    # Actualizar la pantalla
    pygame.display.update()
