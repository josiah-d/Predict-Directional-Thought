# imports
import pygame


class bar:
    '''Creates a bar to track the right and wrong predictions'''

    def __init__(self, screen, color, left, width=750, red=False):
        '''
        initialie bar

        params
        ======
        screen(pygame.screen): screen to display on
        width(int): sets the width of the bar
        color(list): RGB for the color of the bar
        left(int): set the x location
        red(bool): control logic if the bar is for the errant predicitons

        attrs
        =====
        none

        returns
        =======
        none
        '''
        self.screen = screen
        self.width = width
        self.color = color
        self.left = left
        self.red = red

    def check_width_left(self):
        '''
        ensures proper display to ensure the bar remains with the bounds

        params
        ======
        none

        attrs
        =====
        none

        returns
        =======
        none
        '''
        if self.left <= 55 and self.red:
            self.left = 55
        if self.width >= 1495:
            self.width = 1495
        elif self.width <= 5:
            self.width = 5

    '''
    /**
    * todo: rework `increase_width` and `decrease_width` to scale by the percentage right or wrong
    **/
    '''

    def increase_width(self):
        '''
        increase the width of the bar

        for example, if the prediction is correct, the green bar increases by 5
        and the red bar decreases by 5

        params
        ======
        none

        attrs
        =====
        none

        returns
        =======
        none
        '''
        self.check_width_left()
        self.width += 15
        if self.red:
            self.left -= 15

    def decrease_width(self):
        '''
        decrease the width of the bar

        for example, if the prediction is incorrect, the green bar decreases by 5
        and the red bar increases by 5

        params
        ======
        none

        attrs
        =====
        none

        returns
        =======
        none
        '''
        self.check_width_left()
        self.width -= 15
        if self.red:
            self.left += 15

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
        '''
        pygame.draw.rect(self.screen, self.color,
                         (self.left, 50, self.width, 10))
