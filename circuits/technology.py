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

    def __init__(self, name, circuit, cost):
        self.name = name
        self.circuit = circuit
        self.cost = cost

    def satisfies(self, goal):
        '''
        Determine whether this instances exactly implements a goal tech.
        '''
        return self.distance_from(goal) == 0

    def better_than(self, other, goal):
        '''
        Determine whether this instance approximates a goal tech better than
        some other `Technology` instance.
        '''
        own_dist = self.distance_from(goal)
        other_dist = other.distance_from(goal)
        if own_dist != other_dist:
            return own_dist < other_dist
        return self.cost < other.cost

    def distance_from(self, goal):
        '''
        Distance is the number of possible inputs for which the output of the
        circuit differs from that of the goal circuit. Smaller values are
        better.
        '''
        pass

    def combined_with(self, other):
        '''
        Combine with another `Technology` instance and return the resulting,
        new tech.
        '''
        pass
