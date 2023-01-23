import arcade
from sprites.bar import bar
from arcade.experimental.crt_filter import CRTFilter
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, RESOLUTION_DOWN_SCALE, HARD_SCAN, HARD_PIX, DISPLAY_WARP, MASK_DARK, MASK_LIGHT


class game_view(arcade.View):
    def __init__(self):
        super().__init__()

        arcade.set_background_color(arcade.color.BLACK)

        self.sprite_list = None
        self.bar1 = None
        self.bar2 = None

    def setup(self):

        self.crt_filter = CRTFilter(SCREEN_WIDTH, SCREEN_HEIGHT, RESOLUTION_DOWN_SCALE,
                                    HARD_SCAN, HARD_PIX, DISPLAY_WARP, MASK_DARK, MASK_LIGHT)
        self.filter_on = True
        self.sprite_list = arcade.SpriteList()

        self.bar1 = bar("player_1")
        self.bar2 = bar("player_2")
        self.bar1.setup(center_x=50)
        self.bar2.setup(center_x=SCREEN_WIDTH-50)
        self.sprite_list.extend([self.bar1, self.bar2])

    def on_draw(self):
        self.crt_filter.use()
        self.crt_filter.clear()

        self.sprite_list.draw()
        self.draw_mid_dashed_line()

        self.window.use()
        self.clear()
        self.crt_filter.draw()

    def on_update(self, delta_time):
        self.sprite_list.update()

    def on_key_press(self, key, key_modifiers):
        self.bar1.on_key_press(key, key_modifiers)
        self.bar2.on_key_press(key, key_modifiers)

    def on_key_release(self, key, key_modifiers):
        self.bar1.on_key_release(key, key_modifiers)
        self.bar2.on_key_release(key, key_modifiers)

    def draw_mid_dashed_line(self):
        mid = SCREEN_WIDTH/2
        points = []

        for x in range(0, SCREEN_HEIGHT, SCREEN_HEIGHT//50):
            points.append([mid, x])

        arcade.draw_lines(points, arcade.color.WHITE, 5)
