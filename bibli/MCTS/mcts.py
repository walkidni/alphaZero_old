import random
from .Selection import select
from .Node import Node as nd
from .Simulation import simulate
from .Backprop import Backpagation as bp
from .Expansion import expand
from . import VERBOSE


class MCTS:
    def __init__(self, root_node, c1=0.2, c2=None):
        self.root = root_node
        self.c1 = c1
        self.c2 = c2
        return

    def iteration(self):
        # Selection
        current_node = self.root

        # current_node.print('current node')
        while not current_node.state.is_terminal() and current_node.children:
            # print('selection')
            current_node = select(current_node)
        # Expansion
        if not current_node.state.is_terminal():
            children = expand(current_node)
            current_node = random.choice(children)
        # Simulation
        winner = simulate(current_node)
        # Backpropagation
        bp.backpropagate(current_node, winner, self.root.state.m_color)
        # print('finition')
        best_child = select(self.root)
        return best_child

    def move(self, n_iters):
        "Runs the MCTS algorithm iteration *n_iters* times to get an optimal move to play"
        assert n_iters >= 1
        for _ in range(n_iters-1):
            self.iteration()

        node = self.iteration()

        if VERBOSE:
            print('MTCS move node :')
        node.print('move-node', VERBOSE)
        # print(node.parent)
        move = node.move
        # print(move)
        return move
