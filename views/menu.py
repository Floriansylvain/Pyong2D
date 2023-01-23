import arcade
import arcade.gui
from views.game import game_view
from arcade.experimental.crt_filter import CRTFilter
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, RESOLUTION_DOWN_SCALE, HARD_SCAN, HARD_PIX, DISPLAY_WARP, MASK_DARK, MASK_LIGHT


class menu_view(arcade.View):
    def __init__(self):
        super().__init__()

        arcade.set_background_color(arcade.color.BLACK)

        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        button_style = {
            "font_name": "consolas",
            "font_size": 20,
            "font_color": arcade.color.WHITE,
            "border_width": 4,
            "border_color": arcade.color.WHITE,
            "bg_color": arcade.color.BLACK,
            "bg_color_pressed": arcade.color.WHITE,
            "font_color_pressed": arcade.color.BLACK
        }
        start_button = arcade.gui.UIFlatButton(
            text="Start Game", width=200, style=button_style)
        settings_button = arcade.gui.UIFlatButton(
            text="Settings", width=200, style=button_style)
        quit_button = arcade.gui.UIFlatButton(
            text="Quit", width=200, style=button_style)

        start_button.on_click = self.on_click_start
        settings_button.on_click = self.on_click_settings
        quit_button.on_click = self.on_click_quit

        self.v_box = arcade.gui.UIBoxLayout()
        self.v_box.add(start_button.with_space_around(bottom=20))
        self.v_box.add(settings_button.with_space_around(bottom=20))
        self.v_box.add(quit_button)

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )

    def on_click_start(self, event):
        newGame = game_view()
        newGame.setup()
        self.window.show_view(newGame)

    def on_click_settings(self, event):
        pass

    def on_click_quit(self, event):
        arcade.close_window()

    def setup(self):
        self.crt_filter = CRTFilter(SCREEN_WIDTH, SCREEN_HEIGHT, RESOLUTION_DOWN_SCALE,
                                    HARD_SCAN, HARD_PIX, DISPLAY_WARP, MASK_DARK, MASK_LIGHT)

        self.filter_on = True

    def on_draw(self):
        self.crt_filter.use()
        self.crt_filter.clear()
        self.manager.draw()

        self.window.use()
        self.clear()
        self.crt_filter.draw()

    def on_update(self, delta_time):
        pass
