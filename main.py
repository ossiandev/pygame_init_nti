import pygame

pygame.init()

screenHeight = 800

screenWidth = 600

screen = pygame.display.set_mode((screenWidth,screenHeight))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()