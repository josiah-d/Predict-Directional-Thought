import time

import numpy as np

import arrows
import pygame

# initialize pygame
pygame.init()

# create screen
screen = pygame.display.set_mode((1600, 900))

# add title
pygame.display.set_caption('Using an OpenBCI to Predict Directional Thought')

# predictions and test data
y_pred = np.random.choice(['l', 'n', 'r'], 100)
y_test = np.random.choice(['l', 'n', 'r'], 100)

# score bar
green_width = 0
red_width = 0

# create text
font = pygame.font.Font('freesansbold.ttf', 64)


def show_text(txt, x, y):
    text = font.render(txt, False, (255, 255, 255))
    screen.blit(text, (x, y))


if __name__ == '__main__':
    # establish quit functionality
    running = True

    # counter to index from y_pred and y_test
    counter = 0

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

        # highlight from tets
        if y_test[counter] == 'l':
            arrows.left_small.load_arrow(screen)
        if y_test[counter] == 'n':
            arrows.none_small.load_arrow(screen)
        if y_test[counter] == 'r':
            arrows.right_small.load_arrow(screen)

        # add right wrong bar
        if y_pred[counter] == y_test[counter]:
            green_width += 5
        else:
            red_width += 5
        pygame.draw.rect(screen, (0, 255, 0),
                         (50, 50, green_width, 10))  # green
        pygame.draw.rect(screen, (255, 0, 0), (50, 65, red_width, 10))  # red

        # Monitor key presses
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # update counter
        counter += 1

        # add text
        show_text('y_test', 50, 225)
        show_text('y_pred', 50, 550)

        # update loop
        pygame.display.update()
        time.sleep(0.1)
