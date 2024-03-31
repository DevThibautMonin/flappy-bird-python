import pygame
import os

pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flappy Bird")

run = True

# Load images
dirname = os.path.dirname(__file__)
background_path = os.path.join(dirname, "../assets/background.png")
background = pygame.image.load(background_path)

while run:

  screen.blit(background, (0, 0))

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  pygame.display.update()

pygame.quit()
