from . import  VERBOSE
from .Node import Node
import jsonpickle as jp


def expand(node):
    if VERBOSE: print('Expansion on:')
    node.print('expand_node-node', VERBOSE)
    children = []
    for move in node.state.legal_moves():
        child = Node(
            state=node.state.resulting_state(move),
            parent=node,
        )
        # print(jp.encode(child))
        children.append(child)
        node.children.append(child)
        # child.print('expand-child', True)
        # assert False
            
    return children
