import pygame, sys, random
from pygame.math import Vector2


pygame.init()



color = (0,255,255)
clock = pygame.time.Clock()
(CELL_SIZE, CELL_QTY) = (40, 20)
surface = pygame.display.set_mode((CELL_SIZE * CELL_QTY, CELL_SIZE * CELL_QTY))


on = True
class FRUIT:
    def __init__(self):
        self.x = random.randint(1, 20)
        self.y = random.randint(1, 20)
        self.pos = Vector2(self.x, self.y)

    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x * CELL_SIZE, self.pos.y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(surface, (255,0,0), fruit_rect)


class SNAKE:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.pos = Vector2(self.x, self.y)

    def spawn_snake(self):
        snake_rect = pygame.Rect(self.pos.x * CELL_SIZE, self.pos.y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(surface, (0,255,0), snake_rect)








fruit = FRUIT()
snake = SNAKE()
pygame.display.set_caption("Python Snake")


while on: 
    for e in pygame.event.get():
        
        if e.type == pygame.QUIT:
            print(f"{e.type} event... which is == {pygame.QUIT}")
            on = False
        if e.type == pygame.KEYDOWN:
            print("key")
            if e.key == pygame.K_w:
                print("trying to go up")
                snake.pos += Vector2(0, -1)   
            if e.key == pygame.K_s:
                print("trying to go down")
                snake.pos += Vector2(0, 1)   
            if e.key == pygame.K_a:
                print("trying to go left")
                snake.pos += Vector2(-1, 0)   
            if e.key == pygame.K_d:
                print("trying to go right")
                snake.pos += Vector2(1, 0)    
    surface.fill(color)
    fruit.draw_fruit()
    snake.spawn_snake()
    pygame.display.flip()
    clock.tick(60)

