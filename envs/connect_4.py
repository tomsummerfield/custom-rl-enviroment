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
    
# Check if player has won
def has_player_won(move, player):
    
    has_won = check_win_left_horizontal(move, player)
    if has_won:
        print(f"Player {player} has won by left horizontal")
        return True
    has_won = check_win_right_horizontal(move, player)
    if has_won:
        print(f"Player {player} has won by right horizontal")
        return True
    has_won = check_win_vertical_up(move, player)
    if has_won:
        print(f"Player {player} has won by vertical up")
        return True
    has_won = check_win_vertical_bottom(move, player)
    if has_won:
        print(f"Player {player} has won by vertical bottom")
        return True
    has_won = check_win_diagonal_up_right(move, player)
    if has_won:
        print(f"Player {player} has won by diaganol up right")
        return True
    has_won = check_win_diagonal_up_left(move, player)
    if has_won:
        print(f"Player {player} has won by diaganol up left")
        return True
    has_won = check_win_diagonal_down_left(move, player)
    if has_won:
        print(f"Player {player} has won by diaganol down left")
        return True
    has_won = check_win_diagonal_down_right(move, player)
    if has_won:
        print(f"Player {player} has won by diaganol down right")
        return True
    
    return False
    
# Defined functions to check if user has won
def check_win_left_horizontal(move, player):
    
    left = 0
    starting_position = move[1]
    connect_count = 0
    index = 0
    
    while starting_position >= left:
        player_index = move[0], move[1] - index
        player_at_index = connect_2d_board[player_index]
        if player_at_index == player:
            connect_count +=1
            index +=1
            starting_position -=1
        else:
            break
    
    if connect_count == 4:
        return True
    
    return False
    
def check_win_right_horizontal(move, player):
    right = 6
    starting_position = move[1]
    connect_count = 0
    index = 0
    
    while starting_position <= right:
        player_index = move[0], move[1] + index
        player_at_index = connect_2d_board[player_index]
        if player_at_index == player:
            connect_count +=1
            index +=1
            starting_position +=1
        else:
            break
    
    if connect_count == 4:
        return True
    
    return False

def check_win_vertical_up(move, player):
    top = 0
    starting_position = move[0]
    connect_count = 0
    index = 0
    
    while starting_position >= top:
        player_index = move[0] - index, move[1]
        player_at_index = connect_2d_board[player_index]
        if player_at_index == player:
            connect_count +=1
            index +=1
            starting_position -=1
        else:
            break
    
    if connect_count == 4:
        return True
    
    return False
    
def check_win_vertical_bottom(move, player):
    bottom = 5
    starting_position = move[0]
    connect_count = 0
    index = 0
    
    while starting_position <= bottom:
        player_index = move[0] + index, move[1]
        player_at_index = connect_2d_board[player_index]
        if player_at_index == player:
            connect_count +=1
            index +=1
            starting_position +=1
        else:
            break
    
    if connect_count == 4:
        return True
    
    return False

def check_win_diagonal_up_right(move, player):

    count = 1

    try:
        second_adjacent_move_above = move[0] - 1, move[1] + 1
        if second_adjacent_move_above[0] >= 0:
            if connect_2d_board[tuple(second_adjacent_move_above)] == player:
                count += 1
            third_adjacent_move_above = (
                second_adjacent_move_above[0] - 1,
                second_adjacent_move_above[1] + 1,
            )
            if third_adjacent_move_above[0] >= 0:
                if connect_2d_board[tuple(third_adjacent_move_above)] == player:
                    count += 1
                fourth_adjacent_move_above = (
                    third_adjacent_move_above[0] - 1,
                    third_adjacent_move_above[1] + 1,
                )
                if third_adjacent_move_above[0] >= 0:
                    if connect_2d_board[tuple(fourth_adjacent_move_above)] == player:
                        count += 1

        if count == 4:
            return True
        else:
            return False

    except:
        return False

def check_win_diagonal_up_left(move, player):
    count = 1

    try:
        second_adjacent_move_above = move[0] - 1, move[1] - 1
        if second_adjacent_move_above[0] >= 0 and second_adjacent_move_above[1] >= 0:
            if connect_2d_board[tuple(second_adjacent_move_above)] == player:
                count += 1
            third_adjacent_move_above = (
                second_adjacent_move_above[0] - 1,
                second_adjacent_move_above[1] - 1,
            )
            if third_adjacent_move_above[0] >= 0 and third_adjacent_move_above[1] >= 0:
                if connect_2d_board[tuple(third_adjacent_move_above)] == player:
                    count += 1
                fourth_adjacent_move_above = (
                    third_adjacent_move_above[0] - 1,
                    third_adjacent_move_above[1] - 1,
                )
                if (
                    fourth_adjacent_move_above[0] >= 0
                    and fourth_adjacent_move_above[1] >= 0
                ):
                    if connect_2d_board[tuple(fourth_adjacent_move_above)] == player:
                        count += 1

        if count == 4:
            return True
        else:
            return False

    except:
        return False

def check_win_diagonal_down_left(move, player):
    count = 1
    try:
        second_adjacent_move_above = move[0] + 1, move[1] - 1
        if second_adjacent_move_above[1] >= 0:
            if connect_2d_board[tuple(second_adjacent_move_above)] == player:
                count += 1
            third_adjacent_move_above = (
                second_adjacent_move_above[0] + 1,
                second_adjacent_move_above[1] - 1,
            )
            if third_adjacent_move_above[1] >= 0:
                if connect_2d_board[tuple(third_adjacent_move_above)] == player:
                    count += 1
                fourth_adjacent_move_above = (
                    third_adjacent_move_above[0] + 1,
                    third_adjacent_move_above[1] - 1,
                )
                if fourth_adjacent_move_above[1] >= 0:
                    if connect_2d_board[tuple(fourth_adjacent_move_above)] == player:
                        count += 1

        if count == 4:
            return True
        else:
            return False

    except:
        return False

def check_win_diagonal_down_right(move, player):
    count = 1
    try:
        second_adjacent_move_above = move[0] + 1, move[1] + 1
        if connect_2d_board[tuple(second_adjacent_move_above)] == player:
            count+=1
            third_adjacent_move_above = second_adjacent_move_above[0] + 1, second_adjacent_move_above[1] + 1
            if connect_2d_board[tuple(third_adjacent_move_above)] == player:
                count+=1
                fourth_adjacent_move_above = third_adjacent_move_above[0] + 1, third_adjacent_move_above[1] + 1
                if connect_2d_board[tuple(fourth_adjacent_move_above)] == player:
                    count+=1
                
        if count == 4:
            return True
        else:
            return False
        
    except:
        return False

def env_render():
    print(connect_2d_board)

def switch_player(player):
    
    if player == 1:
        return 2
    else:
        return 1

done = False

# Setted initial player
global player
player = 1

while not done:
    
    # Get move
    if len(moves) > 0:
        
        # Got random move
        move = random.choice(get_possible_moves())
        
        # Made move
        make_move(move, player)
        
        # Render board
        env_render()
        
        # Check if player has won
        has_won = has_player_won(move, player)
        
        if has_won:
            print(f"Player {player} has won")
            done = True
        
        
        # Switch player
        player = switch_player(player)
        
        
    else:
        
        break
