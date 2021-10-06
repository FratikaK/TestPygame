import pygame
from player import Player

# 必ず初期化する
pygame.init()

# スクリーンサイズ
screen = pygame.display.set_mode((500, 500))
# ウィンドウの名前
pygame.display.set_caption("Test Pygame")

# Trueになったらゲームが終了する
done = False

# player.pyから
player = Player("./img/player", 100, 100)

# 画像をpygameにロードさせる
player_image = pygame.image.load(player.get_player_image("mario.jpg"))
screen.blit(player_image, player_image.get_rect())

while not done:
    # どのボタンを押したか
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_DOWN]:
        player.add_location(0, 1)
    if pressed[pygame.K_UP]:
        player.add_location(0, -1)
    if pressed[pygame.K_RIGHT]:
        player.add_location(1, 0)
    if pressed[pygame.K_LEFT]:
        player.add_location(-1, 0)

    # スクリーンを一旦綺麗にする
    screen.fill((0, 0, 0))

    # 画像を表示
    screen.blit(player_image, (player.x_location, player.y_location))
    pygame.display.update()

    # イベント（ボタンを押す、マウスクリックするなど）を取得
    for event in pygame.event.get():
        # ウィンドウを閉じる？　ゲームをやめた場合
        if event.type == pygame.QUIT:
            done = True
