import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Test Pygame")
done = False
x = 60
y = 60

clock = pygame.time.Clock()
clock.tick(60)

while not done:
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_DOWN]:
        y += 1
    if pressed[pygame.K_UP]:
        y -= 1
    if pressed[pygame.K_RIGHT]:
        x += 1
    if pressed[pygame.K_LEFT]:
        x -= 1
    pygame.display.update()
    pygame.time.wait(10)
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(x, y, 90, 90))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.display.flip()
