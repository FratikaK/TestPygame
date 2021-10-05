class Dice:

    def __init__(self, pygame, dice_image_directory: str, x_location: int, y_location: int):
        self.pygame = pygame
        self.dice_image_directory = dice_image_directory
        self.x_location = x_location
        self.y_location = y_location

    def get_dice_image_point(self, num: int):
        return self.dice_image_directory + "/dice" + str(num) + ".png"
