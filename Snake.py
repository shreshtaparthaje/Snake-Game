import pygame
import random

pygame.init()

screen_width = 1000
screen_height = 750
run = True
screen = pygame.display.set_mode((screen_width, screen_height))

snake = [pygame.Rect(300, 375, 20, 20)]
snake_direction = (1, 0)

clockobject = pygame.time.Clock()
ticks = 7
counter = 0

food_x = random.randint(0, 982)
food_y = random.randint(0, 737)

while run:
    if ticks == 7:
        food = pygame.Rect(700, 375, 10, 10)
    else:
        food = pygame.Rect(food_x, food_y, 10, 10)

    clockobject.tick(ticks)
    screen.fill((0, 0, 0))

    for segment in snake:
        pygame.draw.rect(screen, (255, 165, 0), segment)
    pygame.draw.rect(screen, (0, 255, 0), food)

    key = pygame.key.get_pressed()
    if key[pygame.K_a] or key[pygame.K_LEFT]:
        if snake_direction == (1, 0):
            pass
        else:
            snake_direction = (-1, 0)
    elif key[pygame.K_w] or key[pygame.K_UP]:
        if snake_direction == (0, 1):
            pass
        else:
            snake_direction = (0, -1)
    elif key[pygame.K_d] or key[pygame.K_RIGHT]:
        if snake_direction == (-1, 0):
            pass
        else:
            snake_direction = (1, 0)
    elif key[pygame.K_s] or key[pygame.K_DOWN]:
        if snake_direction == (0, -1):
            pass
        else:
            snake_direction = (0, 1)

    new_head = pygame.Rect(snake[0].x + snake_direction[0] * 20, snake[0].y + snake_direction[1] * 20, 20, 20)

    snake.insert(0, new_head)

    if pygame.Rect(new_head).colliderect(food):
        food_x = random.randint(0, 987)
        food_y = random.randint(0, 737)
        if ticks != 50:
            ticks += 1
        else:
            pass
        counter += 1
    else:
        snake.pop()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
pygame.quit()
