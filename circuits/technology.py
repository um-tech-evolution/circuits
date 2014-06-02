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
        if len(self.circuit) != len(other.circuit):
            return False
        return all([a is b for a, b in zip(self.circuit, other.circuit)])

    def satisfies(self, goal):
        return self == goal

    def better_than(self, other, goal):
        return self.score(goal) > other.score(goal)

    def score(self, goal):
        pass
