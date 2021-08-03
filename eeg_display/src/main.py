# imports
import time

import numpy as np
import pygame

import arrows
from score_bar import bar

# initialize pygame
pygame.init()

# create screen
screen = pygame.display.set_mode((1600, 900))

# add title
pygame.display.set_caption('Using an OpenBCI to Predict Directional Thought')

# predictions and test data
y_pred = np.random.choice(['l', 'n', 'r'], 35250)
y_test = np.random.choice(['l', 'n', 'r'], 35250)

# initialize score bars
red = bar(screen, (255, 0, 0), 800, width=750, red=True)
green = bar(screen, (0, 255, 0), 50, width=750)

left_black = bar(screen, (0, 0, 0), 0, width=55)
right_black = bar(screen, (0, 0, 0), 1550, width=50)

# create text
font = pygame.font.Font('freesansbold.ttf', 64)


def show_text(txt, x, y):
    '''Display text'''
    text = font.render(txt, False, (255, 255, 255))
    screen.blit(text, (x, y))


if __name__ == '__main__':
    # establish quit functionality
    running = True

    # counter to index from y_pred and y_test
    counter = 0
    counter_correct = 0

    # game loop
    while running:
        # display arrows
        arrows.left_off.load_arrow(screen)
        arrows.none_off.load_arrow(screen)
        arrows.right_off.load_arrow(screen)

        arrows.left_small_off.load_arrow(screen)
        arrows.none_small_off.load_arrow(screen)
        arrows.right_small_off.load_arrow(screen)

        # highlight from predictions
        if y_pred[counter] == 'l':
            arrows.left.load_arrow(screen)
        if y_pred[counter] == 'n':
            arrows.none.load_arrow(screen)
        if y_pred[counter] == 'r':
            arrows.right.load_arrow(screen)

        # highlight from tests
        if y_test[counter] == 'l':
            arrows.left_small.load_arrow(screen)
        if y_test[counter] == 'n':
            arrows.none_small.load_arrow(screen)
        if y_test[counter] == 'r':
            arrows.right_small.load_arrow(screen)

        # adjust size of right wrong bar
        if counter < 1000:
            if y_pred[counter] != y_test[counter]:
                green.increase_width()
                red.decrease_width()
                counter_correct += 1
            else:
                green.decrease_width()
                red.increase_width()
        else:
            if y_pred[counter] != y_test[counter]:
                green.increase_width()
                red.decrease_width()
            else:
                green.decrease_width()
                red.increase_width()

        # add right wrong bar
        left_black.draw_rect()
        right_black.draw_rect()
        red.draw_rect()
        green.draw_rect()

        # Monitor key presses
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # update counter
        counter += 1

        # calc percent correct
        perc_correct = counter_correct / counter

        # conver old percentage
        pygame.draw.rect(screen, (0, 0, 0),
                         (1300, 80, 300, 100))
        # add text
        show_text(f'{str(round(perc_correct*100, 2))}%', 1300, 80)
        show_text('y_test', 50, 225)
        show_text('y_pred', 50, 550)

        # update loop
        pygame.display.update()
        time.sleep(0.01)
