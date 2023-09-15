import pygame
import random
import pygame_menu

# Inicializar Pygame
pygame.init()

# Dimensiones de la ventana del juego
WIDTH, HEIGHT = 800, 600

# Colores
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Crear la ventana del juego
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego con Enemigos")

# Reloj para controlar la velocidad de actualización
clock = pygame.time.Clock()

# Clase para representar al jugador
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 50)
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

# Clase para representar a los enemigos
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speed = random.randrange(1, 5)

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > HEIGHT:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speed = random.randrange(1, 5)

# Función para iniciar el juego
def start_game():
    # Grupos de sprites
    all_sprites = pygame.sprite.Group()
    enemies = pygame.sprite.Group()

    # Crear al jugador
    player = Player()
    all_sprites.add(player)

    # Crear enemigos
    for i in range(10):
        enemy = Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)

    # Contador de puntos
    score = 0
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Puntos: {score}", True, WHITE)
    score_rect = score_text.get_rect()
    score_rect.topleft = (10, 10)

    # Tiempo transcurrido desde el inicio del juego
    start_time = pygame.time.get_ticks()

    # Bucle principal del juego
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Calcular el tiempo transcurrido
        elapsed_time = pygame.time.get_ticks() - start_time

        # Actualizar el contador de puntos
        score = elapsed_time // 1000  # 1 punto por cada segundo

        # Actualizar
        all_sprites.update()

        # Colisiones
        hits = pygame.sprite.spritecollide(player, enemies, False)
        if hits:
            running = False

        # Dibujar
        window.fill((0, 0, 0))
        all_sprites.draw(window)

        # Actualizar el texto de puntuación
        score_text = font.render(f"Score: {score}", True, WHITE)
        window.blit(score_text, score_rect)

        pygame.display.flip()

        # Controlar la velocidad de actualización
        clock.tick(60)

    # Regresar al menú de inicio
    menu.mainloop(window)

# Función para salir del juego
def quit_game():
    pygame.quit()
    exit()

# Crear el menú de inicio
menu = pygame_menu.Menu("Defenders of the Realm", WIDTH, HEIGHT)
menu.add.button("Iniciar", start_game)
menu.add.button("Salir", quit_game)

# Bucle principal del menú de inicio
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    window.fill((0, 0, 0))
    menu.mainloop(window)
    pygame.display.flip()

