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
        if isinstance(n, Matrix):
            if self.cols != n.rows:
                raise Exception("Columns of A must match rows of B")

            result = Matrix(self.rows, n.cols)

            for i in range(result.rows):
                for j in range(result.cols):
                    total_sum = 0
                    for k in self.cols:
                        total_sum += self.matrix[i][k] * n.matrix[k][j]
                    result.matrix[i][j] = total_sum

            self.matrix = result.matrix

    def transpose(self):
        result = Matrix(self.cols, self.rows)

        for i in range(result.rows):
            for j in range(result.cols):
                result.matrix[j][i] = self.matrix[i][j]

        return result
