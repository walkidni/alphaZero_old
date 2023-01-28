from bibli import obj_print
from .Selection import uct1


class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.children = []
        self.visits = 0
        self.wins = 0
        self.untried_moves = state.legal_moves()
        self.move = state.last_move
        self.player = state.m_color
        self.uct = 0

    def is_leaf(self):
        return len(self.children) == 0

    def average_reward(self):
        return self.wins / self.visits if self.visits != 0 else 0

    def print(self, context, verbose=True):
        if not verbose: return
        obj_print(self, context)
        
    def update_uct(self, c1=0.2, c2=None):
        if c2:
            self.uct = uct1(self, c1)

    # def __dict__(self):
    #     return self.__dict__