import pygame

pygame.init()


screen = pygame.display.set_mode((640, 480))

base_image = pygame.image.load('base.PNG')
upright_image = pygame.image.load('upright.PNG')
support_image = pygame.image.load('support.PNG')
crossbeam_image = pygame.image.load('crossbeam.PNG')
head_image = pygame.image.load('head.PNG')
body_image = pygame.image.load('body.PNG')
leftArm_image = pygame.image.load('.PNG')
rightArm_image = pygame.image.load('rightArm.PNG')
leftLeg_image = pygame.image.load('leftLeg.PNG')
rightLeg_image = pygame.image.load('rightLeg.PNG')


class HangedMan(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = base_image  # start with the base image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, image):
        self.image = image

# Set up the sprite group
hanged_man_group = pygame.sprite.Group()

# Create the initial sprite and add it to the group
base = HangedMan(100, 100)  # starting position
hanged_man_group.add(base)

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the sprite group with the current image
    current_image = hanged_man[chances]
    base.update(current_image)
    hanged_man_group.draw(screen)

    # Update the display
    pygame.display.update()


pygame.quit()












# import pygame

# base_image = pygame.image.load('base.PNG')



# class HangedMan(pygame.sprite.Sprite):
#     def __init__(self, x, y):
#         super().__init__()
#         self.image = base_image  # start with the base image
#         self.rect = self.image.get_rect()
#         self.rect.x = x
#         self.rect.y = y


# hanged_man_group = pygame.sprite.Group()

# base = HangedMan(100, 100)  # starting position
# hanged_man_group.add(base)


# crossbeam = HangedMan(100, 100)  # same position as base
# crossbeam.image = crossbeam_image  # set the image to the crossbeam image
# hanged_man_group.add(crossbeam)

# hanged_man_group.draw(screen)