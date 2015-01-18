import random

import xo_engine.game as xo_engine


game_field = xo_engine.GameField()
player1 = xo_engine.Player(1, "Vasya", xo_engine.CELL_STATE_X)
player2 = xo_engine.Player(2, "Lesha", xo_engine.CELL_STATE_O)
game = xo_engine.Game(game_field, [player1, player2])
print(player1.as_dict())
print(player2.as_dict())

possible_moves = []
for i in xrange(xo_engine.DEFAULT_FIELD_WIDTH):
    for j in xrange(xo_engine.DEFAULT_FIELD_HEIGHT):
        move = (i, j)
        possible_moves.append(move)

move_counter = 0
while not game.check_game_over():
    if len(possible_moves) == 0:
        break
    random_move_index = random.randint(0, len(possible_moves) - 1)
    print("DEBUG: random_move_index is {}".format(random_move_index))
    random_move = possible_moves.pop(random_move_index)
    x, y = random_move
    if move_counter % 2 == 0:
        game.make_move(player1, x, y)
    else:
        game.make_move(player2, x, y)

    move_counter += 1
    print(str(game_field))
    print(repr(game_field))
    print(game_field.as_dict())

winner = game.get_winner()
print(game.as_dict())
print(game.check_game_over())
if winner == player1:
    print("Player 1 wins! Winner name is {}".format(player1.name))
elif winner == player2:
    print("Player 2 wins! Winner name is {}".format(player2.name))
elif winner is None:
    print("Draw is detected! {} and {} are both loosers:)".format(player1.name,
          player2.name))
else:
    raise Exception("Unexpected get_winner() obtained: {}".format(winner))


