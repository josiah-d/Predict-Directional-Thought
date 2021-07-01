import pygame


class arrow:
    def __init__(self, path, x, y):
        self.arrow = pygame.image.load(path)
        self.x = x
        self.y = y

    def load_arrow(self, screen):
        screen.blit(self.arrow, (self.x, self.y))


# on arrows
left = arrow('img/on/left.png', 300, 450)
none = arrow('img/on/none.png', 672, 450)
right = arrow('img/on/right.png', 1044, 450)

left_small = arrow('img/on/left0.5.png', 364, 194)
none_small = arrow('img/on/none0.5.png', 736, 194)
right_small = arrow('img/on/right0.5.png', 1108, 194)

# off arrows
left_off = arrow('img/off/left.png', 300, 450)
none_off = arrow('img/off/none.png', 672, 450)
right_off = arrow('img/off/right.png', 1044, 450)

left_small_off = arrow('img/off/left0.5.png', 364, 194)
none_small_off = arrow('img/off/none0.5.png', 736, 194)
right_small_off = arrow('img/off/right0.5.png', 1108, 194)

'''
# add arrows
left = pygame.image.load('img/on/left.png')
left_x, left_y = 300, 450

none = pygame.image.load('img/on/none.png')
none_x, none_y = 672, 450

right = pygame.image.load('img/on/right.png')
right_x, right_y = 1044, 450

left_small = pygame.image.load('img/on/left0.5.png')
left_small_x, left_small_y = 364, 194

none_small = pygame.image.load('img/on/none0.5.png')
none_small_x, none_small_y = 736, 194

right_small = pygame.image.load('img/on/right0.5.png')
right_small_x, right_small_y = 1108, 194

load_arrow(left, left_x, left_y)
load_arrow(none, none_x, none_y)
load_arrow(right, right_x, right_y)
load_arrow(left_small, left_small_x, left_small_y)
load_arrow(none_small, none_small_x, none_small_y)
load_arrow(right_small, right_small_x, right_small_y)
'''
