import random


class Perceptron:
    def __init__(self, nodes, learning_rate):
        self.weights = []

        for i in range(nodes):
            self.weights.append(random.choice([-1, 1]))

        self.learning_rate = learning_rate

    def train(self, inputs, desired):
        guess = self.feed_forward(inputs)
        error = desired - guess
        for idx, item in enumerate(self.weights):
            self.weights[idx] = self.learning_rate * error * inputs[idx]

    def feed_forward(self, inputs):
        overall_sum = 0
        for idx, item in enumerate(self.weights):
            overall_sum += inputs[idx] * item

        return self.activate(overall_sum)

    def activate(self, overall_sum):
        if overall_sum > 0:
            return 1
        return -1
