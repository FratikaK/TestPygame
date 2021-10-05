# サイコロを振るアニメーション
# いろんなエフェクト

import pygame

pygame.init()
game_screen = pygame.display.set_mode((1280, 600))
flag = False

clock = pygame.time.Clock()
clock.tick(60)
dice_flag = False

while not flag:

    pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = True
    pygame.display.flip()
