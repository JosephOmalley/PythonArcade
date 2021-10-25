import pygame
pygame.init()


(WIDTH, HEIGHT) = (300, 200)
surface = pygame.display.set_mode((WIDTH, HEIGHT))


color = (0,255,255)

surface.fill(color)
pygame.display.set_caption("Python Snake")
pygame.display.flip()
isrunning = True

while isrunning: 
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            print(f"{e.type} event... which is == {pygame.QUIT}")
            isrunning = False
        if e.type == pygame.KEYDOWN:

            if e.key == pygame.K_w:
                print("trying to go up")
            if e.key == pygame.K_s:
                print("trying to go down")
            if e.key == pygame.K_a:
                print("trying to go left")
            if e.key == pygame.K_d:
                print("trying to go right")    


