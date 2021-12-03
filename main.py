from pygame import *
import sys, pygame
from pygame.locals import *
from pygame.constants import K_ESCAPE, KEYDOWN, QUIT
import Games.snake
mainClock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption("Main Menu")

title = pygame.font.SysFont(None, 73)
option = pygame.font.SysFont(None, 20)


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)



def main_menu():
    screen = pygame.display.set_mode((500, 500),0,32)
    while True:
        screen.fill((0,0,0))
        mx, my = pygame.mouse.get_pos()
        button_1 = pygame.Rect(30, 100, 200, 50)
        #50, 100, 200, 50
        if button_1.collidepoint((mx,my)):
            if pygame.mouse.get_pressed()[0]:
                print("detected")
                Games.snake.start_snake()
        pygame.draw.rect(screen, (200, 100, 0), button_1)
        draw_text("PYTHON ARCADE", title, (255, 255, 255), screen, 250, 50)
        draw_text("Snake", option, (255, 255, 255), screen, 130, 125)
        
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                sys.exit()
            if e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        pygame.display.update()
        mainClock.tick(60)

main_menu()

