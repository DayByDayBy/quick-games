import pygame

pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("My Game")

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # draw your game elements here
    pygame.draw.rect(win, (255, 0, 0), (25, 25, 50, 50))
    pygame.display.update()

pygame.quit()
