# imports
import pygame


class arrow:
    """Draws arrow images"""

    def __init__(self, path, x, y):
        '''Initializes arrow

        params
            x: x location
            y: y location
        '''
        self.arrow = pygame.image.load(path)
        self.x = x
        self.y = y

    def load_arrow(self, screen):
        '''Displays arrow

        params
            screen: screen to display on
        '''
        screen.blit(self.arrow, (self.x, self.y))


# on arrows
# y_pred arrows
left = arrow('../img/on/left.png', 300, 450)
none = arrow('../img/on/none.png', 672, 450)
right = arrow('../img/on/right.png', 1044, 450)

# y_test arrows
left_small = arrow('../img/on/left0.5.png', 364, 194)
none_small = arrow('../img/on/none0.5.png', 736, 194)
right_small = arrow('../img/on/right0.5.png', 1108, 194)

# off arrows
# y_pred arrows
left_off = arrow('../img/off/left.png', 300, 450)
none_off = arrow('../img/off/none.png', 672, 450)
right_off = arrow('../img/off/right.png', 1044, 450)

# y_test arrows
left_small_off = arrow('../img/off/left0.5.png', 364, 194)
none_small_off = arrow('../img/off/none0.5.png', 736, 194)
right_small_off = arrow('../img/off/right0.5.png', 1108, 194)
