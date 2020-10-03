from math import *
import numpy as np
import pygame

PROJECTION_MATRIX = np.array([[1, 0, 0],
                               [0, 1, 0]])

WHITE = [255, 255, 255]


class Cube:
    def __init__(self, pos, side_length, screen):
        self.screen = screen
        self.position = pos
        self.x = self.position[0]
        self.y = self.position[1]
        self.z = self.position[2]
        self.side_length = side_length
        self.half_length = self.side_length / 2
        self.vertices = np.array([
            [self.x - self.half_length, self.y + self.half_length, self.z + self.half_length],
            [self.x + self.half_length, self.y + self.half_length, self.z + self.half_length],
            [self.x + self.half_length, self.y - self.half_length, self.z + self.half_length],
            [self.x - self.half_length, self.y - self.half_length, self.z + self.half_length],
            [self.x - self.half_length, self.y + self.half_length, self.z - self.half_length],
            [self.x + self.half_length, self.y + self.half_length, self.z - self.half_length],
            [self.x + self.half_length, self.y - self.half_length, self.z - self.half_length],
            [self.x - self.half_length, self.y - self.half_length, self.z - self.half_length]])

        self.edges = np.array([[0, 1],
                               [1, 2],
                               [2, 3],
                               [3, 0],
                               [0, 4],
                               [1, 5],
                               [2, 6],
                               [3, 7],
                               [4, 5],
                               [5, 6],
                               [6, 7],
                               [7, 4]])

    def project(self):
        points = []
        for point in self.vertices:
            points.append(np.matmul(PROJECTION_MATRIX, point))
        return points

    def rotate_x(self, degrees):
        old_x = self.x
        old_y = self.y
        old_z = self.z
        self.translate(-self.x, -self.y, -self.z)
        A = radians(degrees)
        rot_mat_x = np.array([[1,       0,       0],
                              [0,  cos(A), -sin(A)],
                              [0,  sin(A), cos(A)]])
        self.vertices = np.matmul(self.vertices, rot_mat_x)
        self.translate(old_x, old_y, old_z)

    def rotate_y(self, degrees):
        old_x = self.x
        old_y = self.y
        old_z = self.z
        self.translate(-self.x, -self.y, -self.z)
        A = radians(degrees)
        rot_mat_y = np.array([[ cos(A), 0, sin(A)],
                              [      0, 1,      0],
                              [-sin(A), 0, cos(A)]])
        self.vertices = np.matmul(self.vertices, rot_mat_y)
        self.translate(old_x, old_y, old_z)

    def rotate_z(self, degrees):
        old_x = self.x
        old_y = self.y
        old_z = self.z
        self.translate(-self.x, -self.y, -self.z)
        A = radians(degrees)
        rot_mat_z = np.array([[cos(A), -sin(A), 0],
                              [sin(A),  cos(A), 0],
                              [     0,       0, 1]])
        self.vertices = np.matmul(self.vertices, rot_mat_z)
        self.translate(old_x, old_y, old_z)

    def translate(self, x, y, z):
        self.position = np.add([x, y, z], self.position)
        self.update_position()
        for i in range(len(self.vertices)):
            self.vertices[i] = np.add([x, y, z], self.vertices[i])

    def update_position(self):
        self.x = self.position[0]
        self.y = self.position[1]
        self.z = self.position[2]

    def draw(self):
        points = self.project()
        for i in range(len(points)):
            pygame.draw.circle(self.screen, WHITE, (int(points[i][0]), int(points[i][1])), 1)
        for edge in self.edges:
            pygame.draw.line(self.screen, WHITE, (int(points[edge[0]][0]), int(points[edge[0]][1])),
                                                 (int(points[edge[1]][0]), int(points[edge[1]][1])))






