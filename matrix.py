import random


class Matrix:
    def __init__(self, rows, cols):
        matrix = []

        self.rows = rows
        self.cols = cols

        for i in range(rows):
            matrix.append([])
            for j in range(cols):
                matrix[i].append(0)

        self.matrix = matrix

    def randomize(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.matrix[i][j] = round(random.uniform(0, 10))

    def add(self, n):
        if isinstance(n, Matrix):
            for i in range(self.rows):
                for j in range(self.cols):
                    self.matrix[i][j] += n.matrix[i][j]

        else:
            for i in range(self.rows):
                for j in range(self.cols):
                    self.matrix[i][j] += n

    def multiply(self, n):
        for i in range(self.rows):
            for j in range(self.cols):
                self.matrix[i][j] *= n
