class Dice:

    def __init__(self, dice_image_directory: str):
        self.dice_image_directory = dice_image_directory

    def get_dice_image(self, num: int):
        return self.dice_image_directory + "/dice" + str(num) + ".jpg"
