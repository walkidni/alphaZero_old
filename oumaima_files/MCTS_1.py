# https://github.com/ai-boson/mcts

import numpy as np
from collections import defaultdict
import time 
from Goban import * 

newGame = Board()
move = newGame.generate_legal_moves()


class MonteCarloTreeSearchNode():
    def __init__(self, game, parent=None, parent_action=None):
        self.state = game
        self.parent = parent
        self.parent_action = parent_action
        self.children = []
        self._number_of_visits = 0
        self._results = defaultdict(int)
        self._results[1] = 0
        self._results[-1] = 0
        self._untried_actions = None
        self._untried_actions = self.untried_actions()

        return

    def untried_actions(self):
        self._untried_actions = self.get_legal_actions()
        return self._untried_actions

    def q(self):
        wins = self._results[1]
        loses = self._results[-1]
        return wins - loses

    def n(self):
        return self._number_of_visits

    def expand_bis(self, index):
    
        action = self._untried_actions[index]
        new_board = self.state 
        new_board.push(action)
        next_state = new_board
        child_node = MonteCarloTreeSearchNode(
		    next_state, parent=self, parent_action=action)

        self.children.append(child_node)
        return child_node 

    def expand(self): 
        for i in range(len(self._untried_actions)):
            print(i) 
            child_node = self.expand_bis(i)
            print("les actions qui n'ont pas encore été faite", len(self._untried_actions))
            self.untried_actions()
            self._untried_actions.pop(i)
            

    def is_terminal_node(self):
        return self.state._gameOver

    def rollout(self):
        current_rollout_state = self.state
        print(current_rollout_state._board)
        while not current_rollout_state.is_game_over():
        
            possible_moves = self.get_legal_actions()
            action = self.rollout_policy(possible_moves)
            self.move(action)

        return current_rollout_state.result()
        
    def reward(self):
        self.rol = self.rollout()
        liste_value = []
        liste_value.append(self.rol)
        best_el = np.max(np.array(liste_value), axis=0)

    def backpropagate(self, result):
        self._number_of_visits += 1.
        self._results[result] += 1.
        if self.parent:
            self.parent.backpropagate(result)

    def is_fully_expanded(self):
        return len(self._untried_actions) == 0


    def best_child(self, c_param=0.1):
        choices_weights = [(c.q() / c.n()) + c_param * np.sqrt((2 * np.log(self.n()) / c.n())) for c in self.children]
        return self.children[np.argmax(choices_weights)]

    # value function
    def rollout_policy(self, possible_moves):

        return possible_moves[np.random.randint(len(possible_moves))]
    
    def best_action(self):
        simulation_no = 10
        for i in range(simulation_no):
		
            v = self._tree_policy()
            reward = v.rollout()
            v.backpropagate(reward)
        
	
        return self.best_child(c_param=0.)
        
    # à modifier
    def _tree_policy(self):
        current_node = self
        print(not current_node.is_terminal_node())
        while not current_node.is_terminal_node():
            if not current_node.is_fully_expanded():
                print('current node is not fully expanded')
                return current_node.expand()
            else:
                current_node = current_node.best_child()
        return current_node

    # choose if the MCTS will do SELECTION, EXPANSION, SIMULATION or BACKPROPAGATION
    

    def get_legal_actions(self): 
        '''Modify according to your game or
        needs. Constructs a list of all
        possible states from current state.
        Returns a list.'''
        print(self.state)
        return self.state.generate_legal_moves()
    
    def is_game_over(self):
        '''
        Modify according to your game or 
        needs. It is the game over condition
        and depends on your game. Returns
        true or false
        '''
        return self.state.is_game_over()

    def game_result(self):
        '''
        Modify according to your game or 
        needs. Returns 1 or 0 or -1 depending
        on your state corresponding to win,
        tie or a loss.
        '''
        results = self.state.result()
        if(results == "1-0"):
            return 1
        elif(results == "0-1"): 
            return -1
        else:
            return 0

    def move(self,action):
        '''
        Modify according to your game or 
        needs. Changes the state of your 
        board with a new value. For a normal
        Tic Tac Toe game, it can be a 3 by 3
        array with all the elements of array
        being 0 initially. 0 means the board 
        position is empty. If you place x in
        row 2 column 3, then it would be some 
        thing like board[2][3] = 1, where 1
        represents that x is placed. Returns 
        the new state after making a move.
        '''
        return self.state.push(action)

# def main():
#     root = MonteCarloTreeSearchNode(newGame,None,0)
#     selected_node = root.best_action()
#     return 

root = MonteCarloTreeSearchNode(newGame, None, 0)
  
print(root.best_action())

# policy network outputs move probabilities 
# a value network outputs position evaluation 
