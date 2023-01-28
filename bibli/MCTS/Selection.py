from math import sqrt, log as ln, e, pow
from . import VERBOSE


def uct1(node, c):
    # UCT = Q + c * sqrt(ln(N) / n)
    parent_visits = node.parent.visits if node.parent else pow(e, -100)
    node.uct = node.average_reward() + c #e* sqrt(ln(parent_visits) / node.visits)
    return 
    
def select(node, selection_policy='uct1', c1=0.2, c2=None):
    if VERBOSE : print('Selection on:')
    node.print('select-node', VERBOSE)

    best_child = None
    best_uct = -float("inf")
    for child in node.children:
        node.update_uct(c1, c2)
        uct = node.uct
        # print(uct, best_uct)
        if uct > best_uct:
            best_uct = uct
            best_child = child
    
    # print(best_child)
    
    move = best_child
    # print(move)
    # assert True
    return best_child

# def ucb1(node, c):
#     """
#     Calculate the UCB1 value for the given node.
#     """
#     if node.visits == 1:
#         return float("inf")

#     # Calculate the exploration term
#     exploit = node.accumulated_reward / node.visits
#     explore = math.sqrt(2 * math.log(node.parent.visits) / node.visits)

#     return exploit + c * explore


# def uct2(node, c1, c2):
#     # uct2 = average reward + c1 * sqrt(ln(total number of visits) / number of visits) + c2 * sqrt(ln(total number of visits in the tree)
#     if node.visits == 1:
#         return float("inf")
#     node.print('uct2-node')
#     return node.average_reward() + c1 * sqrt(ln(node.parent.visits) / node.visits) + c2 * sqrt(ln(root.total_visits))


    