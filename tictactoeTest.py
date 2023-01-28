from bibli.TTT.TicTacToe import TicTacToe, Board
from bibli.TTT.Players import MCTSPlayer, RandomPlayer
from bibli.MCTS.Node import Node
from tqdm import tqdm
# state = Board()
# node = Node(state)
# node.print('')
ITERS = 1


cparams = [0.05, 0.2, 0.5, 1, 1.5, 2]

# -1 0 1
p1 = RandomPlayer('Randy')
for c in cparams:
    print(f'preparing results for c = {c}')
    p2 = MCTSPlayer('Monte Carlo', 2000, c)
    game = TicTacToe(p1, p2, True, True)
    results = [0, 0, 0]
    for _ in tqdm(range(ITERS)):
        res = game.start_game()
        # print(res)
        results[res+1] += 1
        if res == 0 : _ -= 1
    print(results)
