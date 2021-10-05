import pygame

from player import Player

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Test Pygame")
done = False
x = 60
y = 60

clock = pygame.time.Clock()
clock.tick(60)

player = Player("./img/player", 100, 100)
player_image = pygame.image.load(player.get_player_image("mario.jpg"))
screen.blit(player_image, player_image.get_rect())

while not done:
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_DOWN]:
        player.add_location(0, 1)
    if pressed[pygame.K_UP]:
        player.add_location(0, -1)
    if pressed[pygame.K_RIGHT]:
        player.add_location(1, 0)
    if pressed[pygame.K_LEFT]:
        player.add_location(-1, 0)
    pygame.display.update()
    pygame.time.wait(10)
    screen.fill((0, 0, 0))
    screen.blit(player_image, (player.x_location, player.y_location))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.display.flip()
