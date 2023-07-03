import numpy
import random

class Connect4:
    def __init__(self):
        pass

# Create 2D board
connect_2d_board = numpy.zeros((6, 7), dtype=int)

# Defined Players
players = {"R": 1, "Y": 2}

# Stored initial moves
moves = [[5, 0], [5, 1], [5, 2], [5, 3], [5, 4], [5, 5], [5, 6]]

# Defined Possible Moves
def get_possible_moves():
    return moves

# Defined actions to make a move
def make_move(move, player):
    if move in moves:
        connect_2d_board[tuple(move)] = player  # Add player to board
        moves.remove(move)  # Remove from list

        # Adding new move to moves list
        new_move = [move[0] - 1, move[1]]
        if new_move[0] > -1:
            moves.append(new_move)

# Defined function to switch player
def switch_player(player):
    if player == 1:
        return 2
    else:
        return 1
    
# Defined function to render the enviroment
def env_render():
    return connect_2d_board
    

# Play game
done = False

# Set initial player, to 1
player = 1

while not done:
    
    if len(moves) > 0:
        # Got random move
        move = random.choice(get_possible_moves())
    else:
        break
    
    # Made move
    make_move(move, player)
    
    # Render board
    print(env_render())
    
    # Switched Player
    player = switch_player(player)

    