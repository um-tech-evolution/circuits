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

    def satisfies(self, goal):
        '''
        Determine whether this instances exactly implements a goal tech.
        '''
        return self.distance_from(goal) == 0

    def better_than(self, other, goal):
        return self.score(goal) > other.score(goal)
    def distance_from(self, goal):
        '''
        Distance is the number of possible inputs for which the output of the
        circuit differs from that of the goal circuit. Smaller values are
        better.
        '''
        pass

    def score(self, goal):
        pass
