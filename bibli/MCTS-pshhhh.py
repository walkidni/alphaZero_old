import random

class MCTS:
  def __init__(self, root, expansion_policy, evaluation_function, selection_policy):
    self.root = root
    self.expansion_policy = expansion_policy
    self.evaluation_function = evaluation_function
    self.selection_policy = selection_policy

  def search(self, iterations):
    for _ in range(iterations):
      node = self.selection_policy(self.root)
      if self.expansion_policy(node):
        node = self.expansion_policy(node)
      score = self.evaluation_function(node)
      self.backpropagate(node, score)

    return self.best_child(self.root)

  def selection_policy(self, node):
    while not self.is_leaf(node):
      node = self.best_child(node)
    return node

  def expansion_policy(self, node):
    if self.is_leaf(node):
      return self.expand(node)
    return None

  def expand(self, node):
    new_node = self.create_child(node)
    node.children.append(new_node)
    return new_node

  def backpropagate(self, node, score):
    while node is not None:
      node.visits += 1
      node.score += score
      node = node.parent

  def best_child(self, node):
    return max(node.children, key=lambda x: x.score / x.visits)

  def is_leaf(self, node):
    return len(node.children) == 0

class Node:
  def __init__(self, parent):
    self.parent = parent
    self.children = []
    self.visits = 0
    self.score = 0

'''
_____________
USAGE FOR GO|
////////////

board = initialize_board()
root = Node(None)
root.board = board

mcts = MCTS(root, expansion_policy, evaluation_function, selection_policy)

while not game_over(board):
  move = mcts.search(iterations)
  make_move(board, move)
  mcts.root = mcts.root.children[move]

print("Final board:")
print(board)
'''