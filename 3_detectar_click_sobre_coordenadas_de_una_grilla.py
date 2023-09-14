import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
ventana_ancho = 400
ventana_alto = 400
ventana = pygame.display.set_mode((ventana_ancho, ventana_alto))
pygame.display.set_caption("Ejemplo de detección de clics en una grilla")

# Definir colores
blanco = (255, 255, 255)
negro = (0, 0, 0)
gris = (200, 200, 200)

# Tamaño de la grilla
filas = 4
columnas = 4
celda_ancho = ventana_ancho // columnas
celda_alto = ventana_alto // filas

# Función para dibujar la grilla
def dibujar_grilla():
    for fila in range(filas):
        for columna in range(columnas):
            x = columna * celda_ancho
            y = fila * celda_alto

            """
            def rect(surface: Surface | SurfaceType,
                 color: Color | Color | int | str | tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int],
                 rect: Rect | RectType | tuple[float | int, float | int, float | int, float | int] | tuple[tuple[float, float] | Sequence[float] | Vector2 | Vector2, tuple[float, float] | Sequence[float] | Vector2 | Vector2] | Sequence[float | int] | Sequence[tuple[float, float] | Sequence[float] | Vector2 | Vector2] | _HasRectAttribute,
                 width: int = 0,
                 border_radius: int = -1,
                 border_top_left_radius: int = -1,
                 border_top_right_radius: int = -1,
                 border_bottom_left_radius: int = -1,
                 border_bottom_right_radius: int = -1)
            """
            pygame.draw.rect(ventana, gris, (x, y, celda_ancho, celda_alto), 1)

# Loop principal del juego
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:  # 1 representa el clic izquierdo del mouse
                # Obtener la posición del clic del mouse
                x, y = pygame.mouse.get_pos()
                # Calcular la celda en la que se hizo clic
                columna_clic = x // celda_ancho
                fila_clic = y // celda_alto
                print(f"Se hizo clic en la celda ({fila_clic}, {columna_clic})")

    # Llenar la ventana con color blanco
    ventana.fill(blanco)

    # Dibujar la grilla
    dibujar_grilla()

    # Actualizar la pantalla
    pygame.display.update()
