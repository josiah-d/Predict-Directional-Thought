# imports
import pygame


class bar:
    '''Creates a bar to track the right and wrong predictions'''

    def __init__(self, screen, color, left, top, width=750, red=False):
        '''
        initialize bar

        params
        ======
        screen(pygame.screen): screen to display on
        width (int): sets the width of the bar
        color (list): RGB for the color of the bar
        left (int): set the x location
        top (int): set the y location
        red (bool): control logic if the bar is for the errant predicitons

        attrs
        =====
        none

        returns
        =======
        none
        '''
        self.screen = screen
        self.color = color
        self.left = left
        self.top = top
        self.width = width
        self.red = red

    def adjust_width(self, percent_right):
        '''
        adjust the width of the bar, scales on percentage of correct predictions

        params
        ======
        percent_right (float): percentage of correct predictions

        attrs
        =====
        none

        returns
        =======
        none
        '''
        if not self.red:
            self.width = int((percent_right) * 1500)

    def draw_rect(self):
        '''
        displays the rectangle on the screen

        params
        ======
        none

        attrs
        =====
        none

        returns
        =======
        none

        Rect(left, top, width, height) -> Rect
        '''
        pygame.draw.rect(self.screen, self.color,
                         (self.left, self.top, self.width, 10))
