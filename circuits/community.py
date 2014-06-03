'''
simulation.py
Primary building blocks for simulations based on the circuit model.
'''


from .primitives import ONE, ZERO, NAND, AND, OR, XOR


class Community:
    '''
    A single innovation community. Within the community, technology sharing
    occurs freely and regularly. New technologies can be composed from old
    technologies as the community attempts to achieve its goals. Serves the
    following purposes:

      * tracks discovered technologies
      * maintains a list of goals
    '''

    def __init__(self, goals=None, technologies=None, primitives=None):
        self._goals = goals or []
        self._technologies = technologies or []
        self._primitives = primitives or [NAND, AND, OR, XOR]
        self._constants = [ONE, ZERO]

    def attempt_invention(self):
        '''
        Attempt to create a new technology, return the technology if
        successful, `None` otherwise.

        Attempts to create a new technology through combination of existing
        technologies, primitives, and constant boolean values.
        '''
        pass

    def satisfies_goal(self, tech):
        '''
        Return the goal best (most closely) satisfied by `tech`.
        '''
        pass

    def add_technology(self, tech):
        '''
        If `tech` is superior to an existing technology at satisfying a goal,
        replace and return the existing technology. Return `None` otherwise.
        '''
        pass

    def already_known(self, tech):
        '''
        Return `True` if `tech` has already been discovered, `False` otherwise.
        '''
        pass
