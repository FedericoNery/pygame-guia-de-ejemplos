import pygame

pygame.init()

# Configuración de la ventana
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Mi Juego")

# Cargar sonido
pygame.mixer.init()
sound = pygame.mixer.Sound("damage.wav")

running = True
enemy = pygame.Rect(300, 100, 50, 50)
enemy_image =pygame.image.load("sprigatito.png")
# Cargar imagen
player_image = pygame.image.load("bulbasaur.png")

# Crear sprite
player = pygame.Rect(100, 100, 50, 50)
window.blit(player_image, player.topleft)
window.blit(enemy_image, enemy.topright)
pygame.display.update()

# Limitar tasa de cuadros por segundo (FPS)
clock = pygame.time.Clock()

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

    if player.colliderect(enemy):
        sound.play()

    window.fill((0, 0, 0))
    window.blit(player_image, player.topleft)
    window.blit(enemy_image, enemy.topright)
    pygame.display.update()
    clock.tick(60)  # Limitar a 60 FPS


"""
Explicacion FPS
Relación entre FPS (Fotogramas por segundo) y el tiempo entre cada fotograma:
FPS (Fotogramas por segundo): Es una medida que indica cuántos cuadros (o imágenes) se muestran en la pantalla cada 
segundo en un videojuego o una aplicación hecha con Pygame. Por ejemplo, si tu juego tiene una tasa de FPS de 60, 
significa que se están mostrando 60 cuadros diferentes en la pantalla cada segundo.

Tiempo entre fotogramas (1 / FPS): Para mantener una tasa de FPS específica, como 60 FPS, necesitas calcular cuánto 
tiempo debe pasar entre cada fotograma. Esto se calcula como el inverso de la tasa de FPS, es decir, 1 dividido por 
el número de FPS. En el caso de 60 FPS, el tiempo entre fotogramas sería de 1/60 segundos, 
que es aproximadamente 16.67 milisegundos.

En un juego con una tasa de FPS de 60, significa que se mostrará un nuevo cuadro en la pantalla cada 16.67 milisegundos. 
Esto asegura una animación suave y fluida, ya que la pantalla se actualiza regularmente a una velocidad constante. 
Si el tiempo entre fotogramas fuera más largo, la animación podría parecer lenta o entrecortada. Si fuera más corto, 
podría sobrecargar el hardware y causar problemas de rendimiento innecesarios. Por lo tanto, controlar la tasa de FPS 
es importante para lograr un equilibrio entre la calidad visual y el rendimiento en tu juego o aplicación en Pygame.
"""