import pygame
import os
import bird

pygame.init()

clock = pygame.time.Clock()
fps = 60

screen_width = 850
screen_height = 850

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flappy Bird")

scroll = 0
scroll_speed = 4

# Load images
dirname = os.path.dirname(__file__)
background_path = os.path.join(dirname, "../assets/background.png")
floor_path = os.path.join(dirname, "../assets/floor.png")
background = pygame.image.load(background_path)
floor = pygame.image.load(floor_path)

bird_group = pygame.sprite.Group()

flappy = bird.Bird(100, int(screen_height / 2))
bird_group.add(flappy)

run = True

while run:

  clock.tick(fps)

  screen.blit(background, (0, 0))

  bird_group.draw(screen)

  screen.blit(floor, (scroll, background.get_height()))
  scroll -= scroll_speed

  if abs(scroll) > 35:
    scroll = 0

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  pygame.display.update()

pygame.quit()
