import pygame
import os
import bird

pygame.init()

clock = pygame.time.Clock()
fps = 60

screen_width = 1000
screen_height = 1000

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flappy Bird")

scroll = 0
scroll_speed = 4
flying = False
game_over = False

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
  bird_group.update(background.get_height(), flying, game_over)

  screen.blit(floor, (scroll, background.get_height()))

  # Game over
  if flappy.rect.bottom > background.get_height():
    game_over = True
    flying = False

  if game_over == False:
    scroll -= scroll_speed
    if abs(scroll) > 35:
      scroll = 0

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
    if event.type == pygame.MOUSEBUTTONDOWN and flying == False and game_over == False:
      flying = True

  pygame.display.update()

pygame.quit()
