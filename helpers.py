import random
from itertools import starmap
from operator import mul


class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for _ in range(self.cols)] for _ in range(rows)]

    def randomize(self):
        self.data = [[round(random.uniform(0, 10)) for _ in range(self.cols)] for _ in range(self.rows)]

    def add(self, a):
        if isinstance(a, Matrix):
            if self.rows == a.rows and self.cols == a.cols:
                self.data = [[self.data[d1][d2] + a.data[d1][d2] for d2 in range(self.cols)] for d1 in range(self.cols)]
            else:
                raise Exception("Matrices is in different dimension")
        else:
            raise Exception("Parameter is not a matrix instance")

    def subtract(self, a):
        if isinstance(a, Matrix):
            if self.rows == a.rows and self.cols == a.cols:
                self.data = [[self.data[d1][d2] - a.data[d1][d2] for d2 in range(self.cols)] for d1 in range(self.cols)]
            else:
                raise Exception("Matrices is in different dimension")
        else:
            raise Exception("Parameter is not a matrix instance")

    def dot(self, a):
        if isinstance(a, Matrix):
            if self.cols == a.rows:
                return [[sum(starmap(mul, zip(row, col))) for col in zip(*a.data)] for row in self.data]
            else:
                return Exception("You cannot multiply these matrix, check the dimension.")
        else:
            raise Exception("Parameter is not a matrix instance")
