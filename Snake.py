# Imports
import pygame
import random
import time

# Variables
pygame.init()

# Screen + Loop Condition
screen_width = 1100
screen_height = 910
run = True
screen = pygame.display.set_mode((screen_width, screen_height))

# Snake + Boarder
snake = [pygame.Rect(300, 415, 20, 20)]
snake_direction = (1, 0)
boarder1 = pygame.Rect(0, 870, 1100, 40)
boarder2 = pygame.Rect(1060, 0, 40, 910)
boarder3 = pygame.Rect(0, 0, 1100, 40)
boarder4 = pygame.Rect(0, 0, 40, 910)

# Snake Pictures
snake_head_right = pygame.image.load(r"C:\Users\shres\PycharmProjects\pythonProject\Images\Snake_Head.png")
snake_head_right = pygame.transform.scale(snake_head_right, (20, 20))
snake_head_left = pygame.image.load(r"C:\Users\shres\PycharmProjects\pythonProject\Images\Snake_Head_Left.png")
snake_head_left = pygame.transform.scale(snake_head_left, (20, 20))
snake_head_up = pygame.image.load(r"C:\Users\shres\PycharmProjects\pythonProject\Images\Snake_Head_Up.png")
snake_head_up = pygame.transform.scale(snake_head_up, (20, 20))
snake_head_down = pygame.image.load(r"C:\Users\shres\PycharmProjects\pythonProject\Images\Snake_Head_down.png")
snake_head_down = pygame.transform.scale(snake_head_down, (20, 20))

snake_body_horizontal = pygame.image.load(r"C:\Users\shres\PycharmProjects\pythonProject\Images\Snake_Body.png")
snake_body_horizontal = pygame.transform.scale(snake_body_horizontal, (20, 20))
snake_body_vertical = pygame.image.load(r"C:\Users\shres\PycharmProjects\pythonProject\Images\Snake_Body_vert.png")
snake_body_vertical = pygame.transform.scale(snake_body_vertical, (20, 20))

# Food
food_x = random.randint(40, screen_width - 40)
food_y = random.randint(40, screen_height - 40)

# Miscellaneous
clockobject = pygame.time.Clock()
ticks = 7
counter = 0
font = pygame.font.Font(None, 50)

# Game Loop
while run:
    # Food Location
    if ticks == 7:
        food = pygame.Rect(700, 420, 10, 10)
    else:
        food = pygame.Rect(food_x, food_y, 10, 10)

    # Game Speed + Screen Fill
    clockobject.tick(ticks)
    screen.fill((0, 0, 0))

    # Drawing the Snake + Boarder
    for segment in snake:
        pygame.draw.rect(screen, (255, 165, 0), segment)
    pygame.draw.rect(screen, (255, 0, 0), food)
    pygame.draw.rect(screen, (255, 255, 255), boarder1)
    pygame.draw.rect(screen, (255, 255, 255), boarder2)
    pygame.draw.rect(screen, (255, 255, 255), boarder3)
    pygame.draw.rect(screen, (255, 255, 255), boarder4)

    # Movement
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

    # New Segments
    new_head = pygame.Rect(snake[0].x + snake_direction[0] * 20, snake[0].y + snake_direction[1] * 20, 20, 20)
    snake.insert(0, new_head)

    for i, segment in enumerate(snake):
        if i == 0:
            if snake_direction == (1, 0):
                screen.blit(snake_head_right, segment)
            elif snake_direction == (-1, 0):
                screen.blit(snake_head_left, segment)
            elif snake_direction == (0, -1):
                screen.blit(snake_head_up, segment)
            elif snake_direction == (0, 1):
                screen.blit(snake_head_down, segment)
        else:
            if snake_direction == (1, 0) or snake_direction == (-1, 0):
                screen.blit(snake_body_horizontal, segment)
            elif snake_direction == (0, -1) or snake_direction == (0, 1):
                screen.blit(snake_body_vertical, segment)

    # Eating Food
    if pygame.Rect(new_head).colliderect(food):
        food_x = random.randint(40, screen_width - 40)
        food_y = random.randint(40, screen_height - 40)
        while any(part.colliderect(pygame.Rect(food_x, food_y, 10, 10)) for part in snake):
            food_x = random.randint(40, screen_width - 40)
            food_y = random.randint(40, screen_height - 40)
        ticks += 1
        counter += 1
    else:
        snake.pop()

    # Score Board
    counter_text = font.render("Score: {}".format(counter), True, (0, 0, 0))
    screen.blit(counter_text, (5, 5))

    # Death by Wall
    if not (40 <= new_head.x < screen_width - 40 and 40 <= new_head.y < screen_height - 40):
        screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 100)
        counter_text = font.render("Score: {}".format(counter), True, (255, 255, 255))
        screen.blit(counter_text, (350, 325))
        pygame.display.update()
        time.sleep(3)
        break

    # Death by Hitting Yourself
    for part in snake[1:]:
        if new_head.colliderect(part):
            screen.fill((0, 0, 0))
            font = pygame.font.Font(None, 100)
            counter_text = font.render("Score: {}".format(counter), True, (255, 255, 255))
            screen.blit(counter_text, (350, 325))
            pygame.display.update()
            time.sleep(3)
            run = False
            break

    # Resetting
    if key[pygame.K_SPACE] or key[pygame.K_RETURN]:
        snake = [pygame.Rect(300, 415, 20, 20)]
        ticks = 7
        counter = 0

    # Quitting
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

    pygame.display.update()

pygame.quit()
