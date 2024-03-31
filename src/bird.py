import pygame
import os

# Load images
dirname = os.path.dirname(__file__)

class Bird(pygame.sprite.Sprite):
  def __init__(self, x, y):
    pygame.sprite.Sprite.__init__(self)
    self.images = []
    self.index = 0
    self.counter = 0
    for num in range(1, 4):
      img = pygame.image.load(os.path.join(dirname, f"../assets/bird{num}.png"))
      self.images.append(img)
    self.image = self.images[self.index]
    self.rect = self.image.get_rect()
    self.rect.center = [x, y]
    self.velocity = 0
    self.clicked = False

  def update(self, height, flying):

    # Gravity
    if flying:
      self.velocity += 0.5
      if self.velocity > 8:
        self.velocity = 8
      if self.rect.bottom < height:
        self.rect.y += int(self.velocity)

    # Jump
    if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
      self.clicked = True
      self.velocity = -10
    if pygame.mouse.get_pressed()[0] == 0:
      self.clicked = False

    # Animation
    self.counter += 1
    flap_cooldown = 5

    if self.counter > flap_cooldown:
      self.counter = 0
      self.index += 1
      if self.index >= len(self.images):
        self.index = 0
    self.image = self.images[self.index]

    # Rotation
    self.image = pygame.transform.rotate(self.images[self.index], self.velocity * -2)
