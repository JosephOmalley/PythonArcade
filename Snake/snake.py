import pygame, sys, random, time
from pygame.math import Vector2


pygame.init()



color = (0,0,0)
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
        self.dirc = "right"
        
    def spawn_snake(self):
            snake_rect = pygame.Rect(self.pos.x * CELL_SIZE, self.pos.y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(surface, (0,255,0), snake_rect)
            
    def move_snake(self):

        
        if self.dirc == "up":
            if 0 <= self.pos.x + 0 <= 19 and 0 <= self.pos.y + -1 <= 19:
                snake.pos += Vector2(0, -1)
        elif self.dirc == "down":
            if 0 <= self.pos.x + 0 <= 19 and 0 <= self.pos.y + 1 <= 19:
                snake.pos += Vector2(0, 1)
        elif self.dirc == "left":
            if 0 <= self.pos.x + -1 <= 19 and 0 <= self.pos.y + 0 <= 19:
                snake.pos += Vector2(-1, 0)
        elif self.dirc == "right":
            if 0 <= self.pos.x + 1 <= 19 and 0 <= self.pos.y + 0 <= 19:
                snake.pos += Vector2(1, 0)
        
        
    
fruit = FRUIT()
snake = SNAKE()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)

pygame.display.set_caption("Python Snake")


while on: 
    for e in pygame.event.get():
        
        if e.type == pygame.QUIT:
            print(f"{e.type} event... which is == {pygame.QUIT}")
            on = False
        if e.type == SCREEN_UPDATE:
            snake.move_snake()

        if e.type == pygame.KEYDOWN:
            print("key")
            if e.key == pygame.K_w:
                print("trying to go up")
                snake.dirc = "up"  
            if e.key == pygame.K_s:
                print("trying to go down")
                snake.dirc = "down"
            if e.key == pygame.K_a:
                print("trying to go left")
                snake.dirc = "left" 
            if e.key == pygame.K_d:
                print("trying to go right")
                snake.dirc = "right"   
    surface.fill(color)
    fruit.draw_fruit()
    snake.spawn_snake()
    pygame.display.flip()
    clock.tick(60)

