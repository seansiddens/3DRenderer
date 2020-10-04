from math import *
import numpy as np
import pygame

PROJECTION_MATRIX = np.array([[1, 0, 0],
                              [0, 1, 0]])


WHITE = [255, 255, 255]




class Sphere:
    def __init__(self, pos, radius, samples, screen):
        self.screen = screen
        self.position = pos
        self.x = self.position[0]
        self.y = self.position[1]
        self.z = self.position[2]
        self.radius = radius
        self.samples = samples
        self.vertices = np.empty(shape=(self.samples, 3))

        phi = pi * (3. - sqrt(5.))  # golden angle in radians

        for i in range(self.samples):
            y = 1 - (i / float(samples - 1)) * 2  # y goes from 1 to -1
            radius = sqrt(1 - y * y)  # radius at y

            theta = phi * i  # golden angle increment

            x = cos(theta) * radius
            z = sin(theta) * radius

            #print(x, y, z)
            x *= self.radius
            y *= self.radius
            z *= self.radius
            self.vertices[i] = [self.position[0] + x, self.position[1] + y, self.position[2] + z]

    def project(self):
        points = []
        for point in self.vertices:
            points.append(np.matmul(PROJECTION_MATRIX, point))
        return points

    def draw(self):
        points = self.project()
        for i in range(len(points)):
            pygame.draw.circle(self.screen, WHITE, (int(points[i][0]), int(points[i][1])), 1)

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


    def translate(self, x, y, z):
        self.position = np.add([x, y, z], self.position)
        self.update_position()
        for i in range(len(self.vertices)):
            self.vertices[i] = np.add([x, y, z], self.vertices[i])


    def update_position(self):
        self.x = self.position[0]
        self.y = self.position[1]
        self.z = self.position[2]


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


class HyperCube:
    def __init__(self, position, side_length, screen):
        self.position = position
        self.x = self.position[0]
        self.y = self.position[1]
        self.z = self.position[2]
        self.w = self.position[3]
        self.side_length = side_length
        self.half_length = self.side_length / 2
        self.screen = screen

        self.vertices = np.array([[ -1, -1,  1,  1],
                                  [  1, -1,  1,  1],
                                  [  1,  1,  1,  1],
                                  [ -1,  1,  1,  1],
                                  [ -1, -1, -1,  1],
                                  [  1, -1, -1,  1],
                                  [  1,  1, -1,  1],
                                  [ -1,  1, -1,  1],
                                  [ -1, -1,  1, -1],
                                  [  1, -1,  1, -1],
                                  [  1,  1,  1, -1],
                                  [ -1,  1,  1, -1],
                                  [ -1, -1, -1, -1],
                                  [  1, -1, -1, -1],
                                  [  1,  1, -1, -1],
                                  [ -1,  1, -1, -1]])
        print(self.vertices.shape)

        # self.vertices = np.array([
        #     [self.x - self.half_length, self.y + self.half_length, self.z + self.half_length, self.w + self.half_length],
        #     [self.x + self.half_length, self.y + self.half_length, self.z + self.half_length, self.w + self.half_length],
        #     [self.x + self.half_length, self.y - self.half_length, self.z + self.half_length, self.w + self.half_length],
        #     [self.x - self.half_length, self.y - self.half_length, self.z + self.half_length, self.w + self.half_length],
        #     [self.x - self.half_length, self.y + self.half_length, self.z - self.half_length, self.w + self.half_length],
        #     [self.x + self.half_length, self.y + self.half_length, self.z - self.half_length, self.w + self.half_length],
        #     [self.x + self.half_length, self.y - self.half_length, self.z - self.half_length, self.w + self.half_length],
        #     [self.x - self.half_length, self.y - self.half_length, self.z - self.half_length, self.w + self.half_length],
        #     [self.x - self.half_length, self.y + self.half_length, self.z + self.half_length, self.w - self.half_length],
        #     [self.x + self.half_length, self.y + self.half_length, self.z + self.half_length, self.w - self.half_length],
        #     [self.x + self.half_length, self.y - self.half_length, self.z + self.half_length, self.w - self.half_length],
        #     [self.x - self.half_length, self.y - self.half_length, self.z + self.half_length, self.w - self.half_length],
        #     [self.x - self.half_length, self.y + self.half_length, self.z - self.half_length, self.w - self.half_length],
        #     [self.x + self.half_length, self.y + self.half_length, self.z - self.half_length, self.w - self.half_length],
        #     [self.x + self.half_length, self.y - self.half_length, self.z - self.half_length, self.w - self.half_length],
        #     [self.x - self.half_length, self.y - self.half_length, self.z - self.half_length, self.w - self.half_length]])

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
                               [7, 4],
                               [0, 8],
                               [1, 9],
                               [2, 10],
                               [3, 11],
                               [4, 12],
                               [5, 13],
                               [6, 14],
                               [7, 15],
                               [8, 9],
                               [9, 10],
                               [10, 11],
                               [11, 8],
                               [12, 13],
                               [13, 14],
                               [14, 15],
                               [15, 12],
                               [8, 12],
                               [9, 13],
                               [10, 14],
                               [11, 15]])

    def gen_matrix(self, w):
        l = 1.9
        matrix = np.zeros(shape=(3, 4))
        matrix[0, 0] = abs((1 / (l - w)))
        matrix[1, 1] = abs((1 / (l - w)))
        matrix[2, 2] = abs((1 / (l - w)))
        return matrix


    def project4D(self):
        points_3d = np.empty(shape=(16, 3))
        for i in range(len(self.vertices)):
            w = self.vertices[i, 3]
            points_3d[i] = np.matmul(self.gen_matrix(w), self.vertices[i])
        return points_3d

    def project3D(self, points_3d):
        points_2d = []
        for point in points_3d:
            points_2d.append(np.matmul(PROJECTION_MATRIX, point))
        return points_2d

    def draw(self):
        points = self.project3D(self.project4D())
        points = np.multiply(100, points)
        points = np.add(points, 350)
        for i in range(len(points)):
            pygame.draw.circle(self.screen, WHITE, (int(points[i][0]), int(points[i][1])), 1)
        for edge in self.edges:
            pygame.draw.line(self.screen, WHITE, (int(points[edge[0]][0]), int(points[edge[0]][1])),
                                                 (int(points[edge[1]][0]), int(points[edge[1]][1])))

    def rotate1(self, degrees):
        A = radians(degrees)
        rot_mat = np.array([[cos(A), -sin(A),      0,           0],
                           [sin(A),  cos(A),      0,           0],
                           [     0,       0, 1,     0],
                           [     0,       0, 0,      1]])
        self.vertices = np.matmul(self.vertices, rot_mat)

    def rotate2(self, degrees):
        A = radians(degrees)
        rot_mat = np.array([[1, 0,      0,           0],
                            [0,  1,      0,           0],
                            [     0,       0, cos(A),     -sin(A)],
                            [     0,       0, sin(A),      cos(A)]])
        self.vertices = np.matmul(self.vertices, rot_mat)

    def rotate_yw(self, degrees):
        A = radians(degrees)
        rot_mat = np.array([[cos(A), 0, -sin(A), 0],
                            [0, 1, 0, 0],
                            [sin(A), 0, cos(A), 0],
                            [0, 0, 0, 1]])
        self.vertices = np.matmul(self.vertices, rot_mat)

    def rotate_xw(self, degrees):
        A = radians(degrees)
        rot_mat = np.array([[1, 0, 0, 0],
                            [0, cos(A), -sin(A), 0, 0],
                            [0, sin(A), cos(A), 1, 0],
                            [0, 0, 0, 1]])
        self.vertices = np.matmul(self.vertices, rot_mat)

    def rotate_zw(self, degrees):
        A = radians(degrees)
        rot_mat = np.array([[cos(A), -sin(A), 0, 0],
                            [sin(A), cos(A), 0, 0],
                            [0, 0, 1, 0],
                            [0, 0, 0, 1]])
        self.vertices = np.matmul(self.vertices, rot_mat)

    def rotate_yz(self, degrees):
        A = radians(degrees)
        rot_mat = np.array([[cos(A), 0, 0, -sin(A)],
                            [0, 1, 0, 0],
                            [0, 0, 1, 0],
                            [sin(A), 0, 0, cos(A)]])
        self.vertices = np.matmul(self.vertices, rot_mat)

    def rotate_xz(self, degrees):
        A = radians(degrees)
        rot_mat = np.array([[1, 0, 0, 0],
                            [0, cos(A), 0, -sin(A)],
                            [0, 0, 1, 0],
                            [0, sin(A), 0, cos(A)]])
        self.vertices = np.matmul(self.vertices, rot_mat)

    def rotate_xy(self, degrees):
        A = radians(degrees)
        rot_mat = np.array([[cos(A), -sin(A), 0, 0],
                            [sin(A),  cos(A), 0, 0],
                            [     0,       0, 1, 0],
                            [     0,       0, 0, 1]])
        self.vertices = np.matmul(self.vertices, rot_mat)

    def translate(self, x, y, z, w):
        self.position = np.add([x, y, z, w], self.position)
        self.update_position()
        for i in range(len(self.vertices)):
            self.vertices[i] = np.add([x, y, z, w], self.vertices[i])

    def update_position(self):
        self.x = self.position[0]
        self.y = self.position[1]
        self.z = self.position[2]
        self.w = self.position[3]
