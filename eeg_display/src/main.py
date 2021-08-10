# imports
import time

import pandas as pd
import pygame

import arrows
from score_bar import bar

# load results
results = pd.read_csv('../../data/best_model_results.csv', index_col=0)
y_true = results['y_true']
y_pred = results['y_pred']

# initialize pygame
pygame.init()

# create screen
screen = pygame.display.set_mode((1600, 900))

# add title
pygame.display.set_caption('Using an OpenBCI to Predict Directional Thought')

# initialize score bars
green = bar(screen, (0, 128, 0), 50, 50, width=750)
red = bar(screen, (255, 0, 0), 50, 50, width=1500, red=True)

# create text
font = pygame.font.Font('freesansbold.ttf', 64)


def show_text(txt, x, y):
    '''
    displays text

    params
    ======
    txt (str): text to display
    x (int): x location
    y (int): y location

    attrs
    =====
    none

    returns
    =======
    none
    '''
    text = font.render(txt, False, (255, 255, 255))
    screen.blit(text, (x, y))


if __name__ == '__main__':
    # establish quit functionality
    running = True

    # counter to index from y_pred and y_true
    counter = 0
    counter_correct = 0

    # game loop
    while running:
        # pause to give time to start a recording
        if counter == 0:
            time.sleep(5)

        # display arrows
        arrows.left_off.load_arrow(screen)
        arrows.none_off.load_arrow(screen)
        arrows.right_off.load_arrow(screen)

        arrows.left_small_off.load_arrow(screen)
        arrows.none_small_off.load_arrow(screen)
        arrows.right_small_off.load_arrow(screen)

        arrows.pointer.load_arrow(screen)

        # highlight from predictions
        if y_pred[counter] == 0:
            arrows.left.load_arrow(screen)
        if y_pred[counter] == 1:
            arrows.none.load_arrow(screen)
        if y_pred[counter] == 2:
            arrows.right.load_arrow(screen)

        # highlight from tests
        if y_true[counter] == 0:
            arrows.left_small.load_arrow(screen)
        if y_true[counter] == 1:
            arrows.none_small.load_arrow(screen)
        if y_true[counter] == 2:
            arrows.right_small.load_arrow(screen)

        # Monitor key presses
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # check for right or worng
        if y_pred[counter] == y_true[counter]:
            counter_correct += 1

        # update counter
        counter += 1

        # calc percent correct
        perc_correct = counter_correct / counter

        # add right wrong bar
        green.adjust_width(perc_correct)
        # red.adjust_width(perc_correct)

        # draw rect
        red.draw_rect()
        green.draw_rect()

        # cover old percentage
        pygame.draw.rect(screen, (0, 0, 0),
                         (1300, 70, 300, 100))

        # add text
        show_text(f'{str(round(perc_correct*100, 2))}%', 1300, 70)
        show_text('y_true', 50, 225)
        show_text('y_pred', 50, 550)
        show_text('baseline', 600, 70)

        # update loop
        pygame.display.update()
        time.sleep(0.05)
