import pygame
import os

# Load images
dirname = os.path.dirname(__file__)
bird_path = os.path.join(dirname, "../assets/bird1.png")
bird = pygame.image.load(bird_path)

class Bird(pygame.sprite.Sprite):
  def __init__(self, x, y):
    pygame.sprite.Sprite.__init__(self)
    self.image = bird
    self.rect = self.image.get_rect()
    self.rect.center = [x, y]
