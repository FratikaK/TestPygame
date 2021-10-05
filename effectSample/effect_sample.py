# サイコロを振るアニメーション
# いろんなエフェクト
import random
import pygame
from pygame.locals import *
from player import Player
from dice import Dice
from square import Square
import square

pygame.init()
game_screen = pygame.display.set_mode((1280, 600))
flag = False

dice_flag = False
dice = Dice(pygame, "./img", 1000, 150)
result = 1

square_iterator = {0: Square(100, 50),
                   1: Square(200, 50),
                   2: Square(300, 50),
                   3: Square(400, 50),
                   4: Square(500, 50),
                   5: Square(600, 50),
                   6: Square(700, 50),
                   7: Square(800, 50),
                   8: Square(800, 150),
                   9: Square(800, 250),
                   10: Square(800, 350),
                   11: Square(800, 450),
                   12: Square(700, 450),
                   13: Square(600, 450),
                   14: Square(500, 450),
                   15: Square(400, 450),
                   16: Square(300, 450),
                   17: Square(200, 450),
                   18: Square(100, 450),
                   19: Square(100, 350),
                   20: Square(100, 250),
                   21: Square(100, 150)
                   }
square_image = pygame.image.load(square.get_image_point())

dice_iterator = [pygame.image.load(dice.get_dice_image_point(1)),
                 pygame.image.load(dice.get_dice_image_point(2)),
                 pygame.image.load(dice.get_dice_image_point(3)),
                 pygame.image.load(dice.get_dice_image_point(4)),
                 pygame.image.load(dice.get_dice_image_point(5)),
                 pygame.image.load(dice.get_dice_image_point(6))]

player = Player(square_iterator[0].x_location, square_iterator[0].y_location, "./player")
player_image = pygame.image.load(player.get_player_image_point("player.jpg"))

print(len(square_iterator))
while not flag:
    # ダイスのアニメーション
    # dice_flagがFalseであればアニメーションしない
    if dice_flag:
        rand = random.randrange(5)
        result = rand
        game_screen.blit(dice_iterator[rand], (dice.x_location, dice.y_location))
    else:
        game_screen.blit(dice_iterator[result], (dice.x_location, dice.y_location))

    # マスの表示
    for sq in square_iterator.values():
        game_screen.blit(square_image, (sq.x_location, sq.y_location))

    # プレイヤーの表示
    game_screen.blit(player_image,
                     (square_iterator[player.get_current_squares()].x_location - 25,
                      square_iterator[player.get_current_squares()].y_location - 25))

    # update
    pygame.display.update()
    game_screen.fill((0, 0, 0))

    # 各イベントの処理
    for event in pygame.event.get():
        if event.type == QUIT:
            flag = True

        if event.type == KEYDOWN:
            pressed = pygame.key.get_pressed()
            # ダイスを振った時
            if pressed[K_SPACE]:
                if dice_flag:
                    dice_flag = False
                    print("出た数は" + str(result + 1) + "だよ！")
                    player.set_current_squares(player.get_current_squares() + result + 1)
                    if player.get_current_squares() >= len(square_iterator):
                        player.set_current_squares(
                            player.get_current_squares() - len(square_iterator)
                        )
                else:
                    dice_flag = True
