# 画面遷移のサンプル
# 方向キーの左または右で画像のセットが切り替わる
import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((1200, 650))
pygame.display.set_caption("Screen Transition")

done = False


def img_point(image_name):
    return "./img/" + image_name + ".png"


# 画像のロード
img = pygame.image
dice1 = img.load(img_point("dice1"))
dice2 = img.load(img_point("dice2"))
dice3 = img.load(img_point("dice3"))
dice4 = img.load(img_point("dice4"))
dice5 = img.load(img_point("dice5"))
dice6 = img.load(img_point("dice6"))
player1 = img.load("./player/player.jpg")
player2 = img.load("./player/luigi.jpg")


def mario_window():
    screen.blit(player1, (600, 300))


def luigi_window():
    screen.blit(player2, (600, 300))


def odd_number_window():
    screen.blit(dice1, (200, 50))
    screen.blit(dice3, (800, 50))
    screen.blit(dice5, (500, 300))


def even_number_window():
    screen.blit(dice2, (600, 50))
    screen.blit(dice4, (800, 50))
    screen.blit(dice6, (500, 300))


i = 0

while not done:
    screen.fill((0, 0, 0))

    if i == 0:
        mario_window()
    elif i == 1:
        even_number_window()
    elif i == 2:
        luigi_window()
    elif i == 3:
        odd_number_window()

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            print("quit window")
            done = True
        if event.type == KEYDOWN:
            pressed = pygame.key.get_pressed()
            if pressed[K_RIGHT]:
                i += 1
                if i >= 4:
                    i = 0
            if pressed[K_LEFT]:
                i -= 1
                if i <= -1:
                    i = 3
