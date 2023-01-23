import arcade
import json
from constants import SCREEN_HEIGHT


class bar(arcade.Sprite):
    __velocity = 15
    __should_move_up = False
    __should_move_down = False
    __player_controls_scheme = None
    __bar_name = ""

    def __init__(self, bar_name):
        super().__init__(filename="assets/bar.jpg", scale=0.25)

        self.__bar_name = bar_name

        with open('controls.json', 'r') as f:
            controls_scheme = json.load(f)
            self.__player_controls_scheme = controls_scheme[self.__bar_name]

    def setup(self, center_x):
        self.center_y = SCREEN_HEIGHT/2
        self.center_x = center_x

    def update(self):
        if self.__should_move_up:
            self.center_y += self.__velocity
        elif self.__should_move_down:
            self.center_y -= self.__velocity

    def on_key_change(self, key, state):
        if key == self.__player_controls_scheme["keyboard"]["up"]:
            self.__should_move_up = state
        elif key == self.__player_controls_scheme["keyboard"]["down"]:
            self.__should_move_down = state

    def on_key_press(self, key, key_modifiers):
        self.on_key_change(key, True)

    def on_key_release(self, key, key_modifiers):
        self.on_key_change(key, False)
