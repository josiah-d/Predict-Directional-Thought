# imports
import pygame


class bar:
    """Creates a bar to track the right and wrong predictions"""

    def __init__(self, screen, color, left, width=750, red=False):
        '''
        Initialize bar

        params
            screen: screen to display on
            width: sets the width of the bar
            color: RGB for the color of the bar
            left: set the x location
            red: control logic if the bar is for the errant predicitons
        '''
        self.screen = screen
        self.width = width
        self.color = color
        self.left = left
        self.red = red

    def check_width_left(self):
        '''Ensures proper display to ensure the bar remains with the bounds'''
        if self.left <= 55 and self.red:
            self.left = 55
        if self.width >= 1495:
            self.width = 1495
        elif self.width <= 5:
            self.width = 5

    def increase_width(self):
        '''Increase the width of the bar

        For example, if the prediction is correct, the green bar increases by 5
        and the red bar decreases by 5
        '''
        self.check_width()
        self.check_left()
        self.width += 5
        if self.red:
            self.left -= 5

    def decrease_width(self):
        '''Decrease the width of the bar

        For example, if the prediction is incorrect, the green bar decreases by 5
        and the red bar increases by 5
        '''
        self.check_width()
        self.check_left()
        self.width -= 5
        if self.red:
            self.left += 5

    def draw_rect(self):
        '''Displays the rectangle on the screen'''
        pygame.draw.rect(self.screen, self.color,
                         (self.left, 50, self.width, 10))
