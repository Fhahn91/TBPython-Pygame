# Module for animal class.
import pygame

class Kitty(pygame.sprite.Sprite) :

    def __init__(self, image):

        pygame.sprite.Sprite.__init__(self)

        self.image = image

        self.rect = self.image.get_rect()


class Puppy(pygame.sprite.Sprite) :

    def __init__(self, image, rectx, recty):

        pygame.sprite.Sprite.__init__(self)

        self.image = image

        self.rect = self.image.get_rect()