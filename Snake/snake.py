
import pygame, sys, random
from pygame.math import Vector2

pygame.init()
gamerunning = True
color = (0,0,0)
clock = pygame.time.Clock()
(CELL_SIZE, CELL_QTY) = (40, 20)
surface = pygame.display.set_mode((CELL_SIZE * CELL_QTY, CELL_SIZE * CELL_QTY))
on = True
font = pygame.font.SysFont(None, 100)
text_surface = font.render('Game Over', True, pygame.Color("red"))
class FRUIT:
    def __init__(self):
        self.eaten()
    
    def eaten(self):
        self.x, self.y = random.randint(0, 19), random.randint(0, 19)
        self.pos = Vector2(self.x, self.y)

    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.x * CELL_SIZE, self.y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(surface, (255,0,0), fruit_rect)


class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10), Vector2(6,10),Vector2(7,10)]
        self.dirc = Vector2(-1,0)
        self.alive = True
        
    def spawn_snake(self):
        for block in self.body:
            x_pos = int(block.x * CELL_SIZE)
            y_pos = int(block.y * CELL_SIZE)
            block_rect = pygame.Rect(x_pos, y_pos, CELL_SIZE,CELL_SIZE)
            pygame.draw.rect(surface,(0,255,0),block_rect)
    
    def eat(self):
        body_copy = self.body[:]
        body_copy.insert(0,body_copy[0] + self.dirc)
        self.body = body_copy[:]
        
            
    def move_snake(self):
        print(self.body[0].y)
        for i in self.body[1:]:
            if i == self.body[0]:
                self.alive = False
                print("snake died")
                
                # now print the text
        if not 0 <= self.body[0].y <= 19.0 or not 0 <= self.body[0].x <= 19.0:
            self.alive = False
                
                
        if snake.body[0] == fruit.pos:
            fruit.eaten()
            self.eat()
            print("yum")
        body_copy = self.body[:-1]
        body_copy.insert(0,body_copy[0] + self.dirc)
        self.body = body_copy[:]
        
            
        # if self.dirc == "up":
        #     if 0 <= self.pos.x + 0 <= 19 and 0 <= self.pos.y + -1 <= 19:
        #         snake.pos += Vector2(0, -1)
        #         self.body_x, self.body_y = 0, -1
        # elif self.dirc == "down":
        #     if 0 <= self.pos.x + 0 <= 19 and 0 <= self.pos.y + 1 <= 19:
        #         snake.pos += Vector2(0, 1)
        #         self.body_x, self.body_y = 0, 1
        # elif self.dirc == "left":
        #     if 0 <= self.pos.x + -1 <= 19 and 0 <= self.pos.y + 0 <= 19:
        #         snake.pos += Vector2(-1, 0)
        #         self.body_x, self.body_y = -1, 0
        # elif self.dirc == "right":
        #     if 0 <= self.pos.x + 1 <= 19 and 0 <= self.pos.y + 0 <= 19:
        #         snake.pos += Vector2(1, 0)
        #         self.body_x, self.body_y = 1, 0
        
        
    
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
                if snake.dirc.y != 1: 
                    print("tryng to go up")
                    snake.dirc.x, snake.dirc.y = 0, -1  
            if e.key == pygame.K_s:
                if snake.dirc.y != -1: 
                    print("trying to go down")
                    snake.dirc.x, snake.dirc.y = 0, 1
            if e.key == pygame.K_a:
                if snake.dirc.x != 1: 
                    print("trying to go left")
                    snake.dirc.x, snake.dirc.y = -1, 0
            if e.key == pygame.K_d:
                print("trying to go right")
                if snake.dirc.x != -1: 
                    snake.dirc.x, snake.dirc.y = 1, 0 
    
    surface.fill(color)
    if snake.alive:
        fruit.draw_fruit()
        snake.spawn_snake()
    else:
        surface.blit(text_surface, [CELL_SIZE * 6, CELL_SIZE * 9])
    pygame.display.flip()
    clock.tick(60)

