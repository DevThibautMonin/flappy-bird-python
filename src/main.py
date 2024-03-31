import pygame
import os
import bird
import pipe
import random

pygame.init()

clock = pygame.time.Clock()
fps = 60

screen_width = 800
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flappy Bird")

scroll = 0
scroll_speed = 4
flying = False
game_over = False
pipe_gap = 150
top_pipe_position = 1
bottom_pipe_position = -1
# Milliseconds
pipe_frequency = 1500
last_pipe = pygame.time.get_ticks() - pipe_frequency

# Load images
dirname = os.path.dirname(__file__)
background_path = os.path.join(dirname, "../assets/background.png")
floor_path = os.path.join(dirname, "../assets/floor.png")
background = pygame.image.load(background_path)
floor = pygame.image.load(floor_path)

bird_group = pygame.sprite.Group()
pipe_group = pygame.sprite.Group()

flappy = bird.Bird(100, int(screen_height / 2))
bird_group.add(flappy)

run = True

while run:

  clock.tick(fps)

  screen.blit(background, (0, 0))

  bird_group.draw(screen)
  bird_group.update(background.get_height(), flying, game_over)
  pipe_group.draw(screen)

  screen.blit(floor, (scroll, background.get_height()))

  # Check for collisions
  if pygame.sprite.groupcollide(bird_group, pipe_group, False, False) or flappy.rect.top < 0:
    game_over = True

  # Game over
  if flappy.rect.bottom >= background.get_height():
    game_over = True
    flying = False

  if game_over == False and flying == True:
    # Generate new pipes
    time_now = pygame.time.get_ticks()
    if time_now - last_pipe > pipe_frequency:
      pipe_height = random.randint(-100, 100)
      bottom_pipe = pipe.Pipe(screen_width, int(screen_height / 2) + pipe_height, bottom_pipe_position, pipe_gap)
      top_pipe = pipe.Pipe(screen_width, int(screen_height / 2) + pipe_height, top_pipe_position, pipe_gap)
      pipe_group.add(bottom_pipe)
      pipe_group.add(top_pipe)
      last_pipe = time_now

    scroll -= scroll_speed
    if abs(scroll) > 35:
      scroll = 0
    pipe_group.update()

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
    if event.type == pygame.MOUSEBUTTONDOWN and flying == False and game_over == False:
      flying = True

  pygame.display.update()

pygame.quit()
