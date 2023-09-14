import pygame
import os

# Inicializar Pygame
pygame.init()

# Definir colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

# Definir la ventana
ventana = pygame.display.set_mode((400, 200))
pygame.display.set_caption("Botonera de Sonidos")

# Cargar los sonidos
sonido1 = pygame.mixer.Sound("mk3-subzero.wav")
sonido2 = pygame.mixer.Sound("clashroyale.ogg")
sonido3 = pygame.mixer.Sound("ryu.wav")

# Función para dibujar los botones
def dibujar_botones():
    pygame.draw.rect(ventana, (255, 0, 0), (50, 50, 100, 50))
    pygame.draw.rect(ventana, (0, 255, 0), (175, 50, 100, 50))
    pygame.draw.rect(ventana, (0, 0, 255), (300, 50, 100, 50))

# Función principal
def main():
    corriendo = True
    while corriendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False
            if evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if 50 <= x <= 150 and 50 <= y <= 100:
                    sonido1.play()
                elif 175 <= x <= 275 and 50 <= y <= 100:
                    sonido2.play()
                elif 300 <= x <= 400 and 50 <= y <= 100:
                    sonido3.play()

        ventana.fill(BLANCO)
        dibujar_botones()
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
