'''
technology.py
Technology abstraction classes and functions.
'''
from random import random, choice
from pyeda.inter import farray
from .constants import INPUT_PROBABILITY


class Technology:
    '''
    A technology, represented by a boolean circuit. Can be compared to other
    technologies for equality and, given a goal, closeness of approximation of
    the goal.

    @param name - the name of the circuit
    @param circuit - a function array
    @param cost - the cost of the circuit
    '''
    def __init__(self, name, circuit, cost=0):
        self.name = name
        self.circuit = circuit
        self.cost = cost

    def satisfies(self, goal):
        '''
        Determine whether this instances exactly implements a goal tech.

        @param goal - the goal to compare against
        '''
        return self.distance_from(goal) == 0

    def better_than(self, other, goal):
        '''
        Determine whether this instance approximates a goal tech better than
        some other `Technology` instance.

        @param other - another technology to compare against
        @param goal - the goal to compare both against
        '''
        own_dist = self.distance_from(goal)
        other_dist = other.distance_from(goal)
        if own_dist != other_dist:
            return own_dist < other_dist
        return self.cost < other.cost

    def distance_from(self, goal):
        '''
        Distance is the number of possible inputs for which the output of the
        technology circuit differs from that of the goal technology. Smaller
        values are better.

        @param goal - the goal technology to compare against
        '''
        pass

    def inputs(self):
        '''
        Return a Python set of the inputs of the circuit.
        '''
        return {inp for expr in self.circuit for inp in expr.inputs}

    def combined_with(self, other):
        '''
        Combine with another `Technology` instance and return the resulting,
        new tech.

        @param other - another technology with which to combine
        '''
        other_exprs = list(other.circuit)
        for other_input in other.inputs():
            if random() < INPUT_PROBABILITY:
                continue
            self_output = choice(self.circuit)
            other_exprs = [expr.compose({other_input: self_output}) for expr in other_exprs]
        self_exprs = list(self.circuit)

        new_name = '{} + {}'.format(self.name, other.name) # TODO Come up with name algorithm
        new_circuit = farray(self_exprs + other_exprs)
        new_cost = self.cost + other.cost # FIXME Compute cost according to A&P

        return Technology(new_name, new_circuit, new_cost)
