import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((1300, 700))
pygame.display.set_caption("Image Movement")

square_plus = pygame.image.load("./square/plus.png")
square_sub = pygame.image.load("./square/sub.png")


class Square:
    def __init__(self, x_location, y_location):
        self.x_location = x_location
        self.y_location = y_location

    def get_image(self):
        pass

    def caught_square(self, player):
        pass

    def display(self):
        pass


class MoneyPlusSquare(Square):
    def __init__(self, x_location, y_location):
        super().__init__(x_location, y_location)
        self.x_location = x_location
        self.y_location = y_location

    def get_image(self):
        return "plus.png"

    def caught_square(self, player):
        player.money += 5

    def display(self):
        screen.blit(square_plus, (self.x_location, self.y_location))


class MoneySubtractionSquare(Square):

    def __init__(self, x_location, y_location):
        super().__init__(x_location, y_location)
        self.x_location = x_location
        self.y_location = y_location

    def get_image(self):
        return "sub.png"

    def caught_square(self, player):
        player.money -= 5
        if player.money < 0:
            player.money = 0

    def display(self):
        screen.blit(square_sub, (self.x_location, self.y_location))


square_iterator = {0: MoneyPlusSquare(20, 10),
                   1: MoneyPlusSquare(60, 10),
                   2: MoneySubtractionSquare(100, 50),
                   3: MoneyPlusSquare(140, 50),
                   4: MoneySubtractionSquare(180, 50),
                   5: MoneyPlusSquare(220, 50),
                   6: MoneySubtractionSquare(260, 50),
                   7: MoneySubtractionSquare(300, 50),
                   8: MoneySubtractionSquare(340, 50),
                   9: MoneyPlusSquare(380, 50),
                   10: MoneyPlusSquare(420, 50),
                   11: MoneyPlusSquare(460, 50),
                   12: MoneySubtractionSquare(500, 50),
                   13: MoneySubtractionSquare(540, 50)}


def square_display():
    for square in square_iterator.values():
        square.display()


class Player(pygame.sprite.Sprite):
    def __init__(self, image_name):
        super(Player, self).__init__()

        self.image = pygame.image.load("./player/" + image_name)
        self.rect = self.image.get_rect()

        # ゲームに関わるステータス
        self.money = 10

    def update(self):
        pass


running = True

while running:
    screen.fill((0, 0, 0))
    square_display()
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            print("quit game")
