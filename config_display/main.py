import pygame
from pygame.locals import *

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 640
TEXT_FONT = "simsunnsimsun"
BUTTON_FONT = "yugothicyugothicuisemiboldyugothicuibold"
TITLE_FONT = "hg創英角ﾎﾟｯﾌﾟ体hgp創英角ﾎﾟｯﾌﾟ体hgs創英角ﾎﾟｯﾌﾟ体"
TEXT_SIZE = 25
TITLE_SIZE = 50

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Test config display")

# Config関連-----------------------------------
title_font = pygame.font.SysFont(TITLE_FONT, TITLE_SIZE)
config_font = pygame.font.SysFont(BUTTON_FONT, TEXT_SIZE)

config_title = title_font.render("Game Setting", True, (255, 255, 255))
config_iterator = [config_font.render("CPUの人数", True, (255, 255, 255)),
                   config_font.render("ターン数", True, (255, 255, 255)),
                   config_font.render("何かの設定", True, (255, 255, 255)),
                   config_font.render("何かの設定", True, (255, 255, 255))]
next_config = config_font.render("次へ", True, (255, 255, 255))
next_select = config_font.render("→", True, (255, 255, 255))

# ゲームの設定の数値
config_num_iterator = [1, 10, 3, 5]

config_select = config_font.render("←     →", True, (255, 255, 255))
now_select = 0
select_location = {0: 100, 1: 130, 2: 160, 3: 190}


def config_display():
    height = 100
    i = 0
    screen.blit(config_title, (500, 30))
    for config in config_iterator:
        num_str = config_font.render(str(config_num_iterator[i]), True, (255, 255, 255))
        screen.blit(config, (400, height))
        screen.blit(num_str, (800, height))
        height += 30
        i += 1
    # やじるし
    screen.blit(config_select, (770, select_location[now_select]))
    # 終了の選択
    screen.blit(next_config, (800, 550))


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
            if pressed[K_LEFT]:
                config_num_iterator[now_select] -= 1
                if config_num_iterator[now_select] < 1:
                    config_num_iterator[now_select] = 1
            if pressed[K_RIGHT]:
                config_num_iterator[now_select] += 1
