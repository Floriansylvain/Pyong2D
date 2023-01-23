import arcade
from views.menu import menu_view
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE


def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = menu_view()
    window.show_view(start_view)
    start_view.setup()
    arcade.run()


if __name__ == "__main__":
    main()
