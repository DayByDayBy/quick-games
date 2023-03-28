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
    pygame.draw.circle(win, (101, 3, 67), (150, 180), 67.00)
    pygame.draw.polygon(win, (145, 25, 255), ((350, 180), (250, 100),  (50, 200)))
    pygame.draw.line(win, (45, 34, 233), (450, 180), (250, 100))
    pygame.display.update()

pygame.quit()
