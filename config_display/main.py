import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((1300, 700))
pygame.display.set_caption("Test config display")
config_font = pygame.font.SysFont("simsunnsimsun", 50)
config_title = config_font.render("ゲームの設定", True, (255, 255, 255))
config_iterator = [config_font.render("CPUの人数", True, (255, 255, 255)),
                   config_font.render("ターン数", True, (255, 255, 255)),
                   config_font.render("何かの設定", True, (255, 255, 255)),
                   config_font.render("何かの設定", True, (255, 255, 255))]
config_num_iterator = [1, 10, 3, 5]
config_select = config_font.render("→", True, (255, 255, 255))
now_select = 0
select_location = {0: 150, 1: 250, 2: 350, 3: 450}


def config_display():
    HEIGHT = 150
    i = 0
    screen.blit(config_title, (300, 50))
    for config in config_iterator:
        num_str = config_font.render(str(config_num_iterator[i]), True, (255, 255, 255))
        screen.blit(config, (100, HEIGHT))
        screen.blit(num_str, (800, HEIGHT))
        HEIGHT += 100
        i += 1
    # やじるし
    screen.blit(config_select, (500, select_location[now_select]))


running = True

while running:
    screen.fill((0, 0, 0))
    config_display()
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            pressed = pygame.key.get_pressed()
            if pressed[K_DOWN]:
                now_select += 1
                if now_select > 3:
                    now_select = 0
            if pressed[K_UP]:
                now_select -= 1
                if now_select < 0:
                    now_select = 3
