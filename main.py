import shapes
from math import *
import numpy as np
import pygame
import sys
import time
np.set_printoptions(suppress=True)


if __name__ == '__main__':
    FPS = 60
    FRAME_TIME = 1 / FPS

    pygame.init()

    size = width, height = 700, 700
    screen = pygame.display.set_mode(size)
    white = [255, 255, 255]

    # print(cube.project())
    # print(len(cube.project()))

    # sphere = shapes.Sphere((width / 2, height / 2, 0), 100, 500, screen)
    # cube = shapes.Cube((width / 2, height / 2, 0), 300, screen)

    hyper_cube = shapes.HyperCube((width / 2, height / 2, 0, 0), 100, screen)

    angle = 1
    while 1:
        time.sleep(FRAME_TIME)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        screen.fill([0, 0, 0])

        # sphere.rotate_y(2)
        # sphere.rotate_x(1)
        #
        # cube.rotate_x(-angle)
        # cube.rotate_z(angle)
        #
        # sphere.draw()
        # cube.draw()

        hyper_cube.rotate_xw(1)
        hyper_cube.draw()


        pygame.display.flip()






