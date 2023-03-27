# this seems like a more fun way to do the images, espcially for showing to the kids.
# plus there is potential to swap out images too, as long as they are named the same
# then it should allow for kids own art to be used.


import pygame


pygame.init()


screen = pygame.display.set_mode((640, 480)).convert()
pygame.display.set_caption('HangMan')


base_image = pygame.image.load('images/base.PNG').convert()
upright_image = pygame.image.load('images/upright.PNG').convert()
support_image = pygame.image.load('images/support.PNG').convert()
crossbeam_image = pygame.image.load('images/crossbeam.PNG').convert()
head_image = pygame.image.load('images/head.PNG').convert()
body_image = pygame.image.load('images/body.PNG').convert()
leftArm_image = pygame.image.load('images/leftArm.PNG').convert()
rightArm_image = pygame.image.load('images/rightArm.PNG').convert()
leftLeg_image = pygame.image.load('images/leftLeg.PNG').convert()
rightLeg_image = pygame.image.load('images/rightLeg.PNG').convert()


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
    current_image = base_image
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