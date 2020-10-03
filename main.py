import shapes
from math import *
import numpy as np
import pygame
import sys
import time
np.set_printoptions(suppress=True)


if __name__ == '__main__':

    def rotate_x(matrix, degrees):
        A = radians(degrees)
        rot_mat_x = np.array([[1,      0,       0],
                              [0, cos(A), -sin(A)],
                              [0, sin(A),  cos(A)]])

        return np.matmul(matrix, rot_mat_x)


    FPS = 60
    FRAME_TIME = 1 / FPS

    pygame.init()

    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)
    white = [255, 255, 255]

    cube = shapes.Cube((width / 2, height / 2, 0), 100, screen)

    angle = 1
    while 1:
        time.sleep(FRAME_TIME)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        screen.fill([0, 0, 0])

        cube.rotate_x(angle)
        cube.rotate_y(angle)
        cube.rotate_z(-angle*2)

        cube.translate(0, sin(pygame.time.get_ticks() / 1000), 0)

        cube.draw()

        pygame.display.flip()






