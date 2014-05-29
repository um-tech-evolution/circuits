'''
technology.py
Technology abstraction classes and functions.
'''


class Technology:
    '''
    A technology, represented by a boolean circuit. Can be compared to other
    technologies for equality and, given a goal, closeness of approximation of
    the goal.
    '''

    def __init__(self, name, circuit):
        self.name = name
        self.circuit = circuit

    def __eq__(self, other):
        pass

    def better_than(self, other, goal):
        return self.score(goal) > other.score(goal)

    def score(self, goal):
        pass
