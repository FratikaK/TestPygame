class Player:

    def __init__(self, x_location, y_location, player_folder: str):
        self.player_folder = player_folder
        self.x_location = x_location
        self.y_location = y_location
        self.current_squares = 0

    def get_player_image_point(self, image_name):
        return self.player_folder + "/" + image_name

    def add_location(self, x, y):
        self.x_location = self.x_location + x
        self.y_location = self.y_location + y

    def set_x_location(self, x_location):
        self.x_location = x_location

    def set_y_location(self, y_location):
        self.y_location = y_location

    # 現在のマスを取得
    def get_current_squares(self):
        return self.current_squares

    # 現在のマスを設定
    def set_current_squares(self, current):
        self.current_squares = current
