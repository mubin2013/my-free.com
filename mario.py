# import pygame
# import sys

# # Инициализация Pygame
# pygame.init()

# # Размеры экрана
# WIDTH, HEIGHT = 800, 600
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption('Простая игра в стиле Марио')

# # Цвета
# WHITE = (255, 255, 255)
# GREEN = (0, 255, 0)
# BLUE = (0, 0, 255)
# BROWN = (139, 69, 19)

# # Гравитация
# GRAVITY = 0.5
# JUMP_STRENGTH = -10

# # Параметры игрока
# player_size = 50
# player_x = WIDTH // 2
# player_y = HEIGHT - player_size
# player_velocity_x = 0
# player_velocity_y = 0
# player_speed = 5

# # Платформы
# platforms = [(0, HEIGHT - 50, WIDTH, 50), (200, HEIGHT - 150, 150, 20), (500, HEIGHT - 300, 150, 20)]

# # Игровой цикл
# clock = pygame.time.Clock()
# running = True

# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()

#     # Управление движением
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_LEFT]:
#         player_velocity_x = -player_speed
#     elif keys[pygame.K_RIGHT]:
#         player_velocity_x = player_speed
#     else:
#         player_velocity_x = 0

#     if keys[pygame.K_SPACE] and player_velocity_y == 0:
#         player_velocity_y = JUMP_STRENGTH

#     # Обновление позиции игрока
#     player_x += player_velocity_x
#     player_y += player_velocity_y
#     player_velocity_y += GRAVITY

#     # Проверка на столкновение с платформами
#     player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
#     for plat in platforms:
#         plat_rect = pygame.Rect(plat)
#         if player_rect.colliderect(plat_rect) and player_velocity_y > 0:
#             player_y = plat[1] - player_size
#             player_velocity_y = 0

#     # Отрисовка
#     screen.fill(WHITE)

#     # Отрисовка платформ
#     for plat in platforms:
#         pygame.draw.rect(screen, BROWN, pygame.Rect(plat))

#     # Отрисовка игрока
#     pygame.draw.rect(screen, BLUE, player_rect)

#     # Обновление экрана
#     pygame.display.flip()
#     clock.tick(60)


import pygame
import sys

# Инициализация Pygame
pygame.init()

# Размеры экрана
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Динозаврик')

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Параметры динозавра
dino_size = 100
dino_x = 50
dino_y = HEIGHT - dino_size - 50
dino_velocity_y = 0
dino_jump = -10
dino_gravity = 0.5
is_jumping = False

# Параметры препятствий
obstacle_width = 20
obstacle_height = 40
obstacle_x = WIDTH
obstacle_y = HEIGHT - obstacle_height - 50
obstacle_velocity = -5

# Гравитация
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Управление движением динозавра
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and not is_jumping:
        is_jumping = True
        dino_velocity_y = dino_jump

    # Обновление позиции динозавра
    if is_jumping:
        dino_y += dino_velocity_y
        dino_velocity_y += dino_gravity
        if dino_y >= HEIGHT - dino_size - 50:
            dino_y = HEIGHT - dino_size - 50
            is_jumping = False
            dino_velocity_y = 0

    # Обновление позиции препятствий
    obstacle_x += obstacle_velocity
    if obstacle_x < -obstacle_width:
        obstacle_x = WIDTH
        obstacle_height = 40  # случайная высота

    # Проверка на столкновение
    dino_rect = pygame.Rect(dino_x, dino_y, dino_size, dino_size)
    obstacle_rect = pygame.Rect(obstacle_x, obstacle_y, obstacle_width, obstacle_height)
    if dino_rect.colliderect(obstacle_rect):
        print("Game Over!")
        pygame.quit()
        sys.exit()

    # Отрисовка
    screen.fill(WHITE)
    pygame.draw.rect(screen, GREEN, pygame.Rect(dino_x, dino_y, dino_size, dino_size))
    pygame.draw.rect(screen, BLACK, pygame.Rect(obstacle_x, obstacle_y, obstacle_width, obstacle_height))

    # Обновление экрана
    pygame.display.flip()
    clock.tick(60)