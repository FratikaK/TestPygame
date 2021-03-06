class Player:

    def __init__(self, player_image_folder: str, x_location: int, y_location: int):
        self.player_image_folder = player_image_folder
        # 画像を貼る座標
        self.x_location = x_location
        self.y_location = y_location

    # 画像の場所を取得する
    def get_player_image(self, image_name: str):
        return self.player_image_folder + "/" + image_name

    def set_location(self, x: int, y: int):
        self.x_location = x
        self.y_location = y

    def add_location(self, x: int, y: int):
        self.x_location = self.x_location + x
        self.y_location = self.y_location + y
