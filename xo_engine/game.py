CELL_STATE_EMPTY = "."
CELL_STATE_X = "X"
CELL_STATE_O = "O"
AVAILABLE_CELL_STATES = set([
    CELL_STATE_EMPTY,
    CELL_STATE_X,
    CELL_STATE_O
])


DEFAULT_FIELD_WIDTH = 3
DEFAULT_FIELD_HEIGHT = 3


class GameField(object):
    """Represents game field, game
    cells container.
    """
    def __init__(self, width=DEFAULT_FIELD_WIDTH,
            height=DEFAULT_FIELD_HEIGHT,
            field=None):
        self.width = width
        self.height = height
        self._field = field
        self._init_field()


    def _init_field(self):
        if self._field is not None:
            return

        self._field = []
        for i in xrange(self.width):
            row = []
            for j in xrange(self.height):
                row.append(CELL_STATE_EMPTY)
            self._field.append(row)


    def __getitem__(self, index):
        """g.__getitem__(index) <==> g[index]
        """
        return self._field[index]


    def __str__(self):
        """Human readable representation of the
        game field.
        """
        row_as_str = []
        for row in self._field:
            row_as_str.append(" ".join(row))

        return "\n".join(row_as_str)


    def __repr__(self):
        """Python readable representation of the game field.
        """
        return str(self.__class__.__name__) + "({}, {}, {})".format(self.width, self.height, self._field)

    def as_dict(self):
        game_field_info = {
            "cells": self._field,
            "width": self.width,
            "height": self.height,
        }
        return game_field_info



class Player(object):
    """Represents game player, which makes
    some steps on the game field.
    """
    def __init__(self, id, name, cell_state):
        self.id = id
        self.name = name
        self.cell_state = cell_state

    def as_dict(self):
        player_info = {
            "id": self.id,
            "name": self.name,
            "cell_state": self.cell_state,
        }
        return player_info


class Game(object):
    """Represents single game of players on some
    game field.
    """
    def __init__(self, game_field, player_list):
        self.game_field = game_field
        self.player_list = player_list
        self._state_to_player_map = {
            player.cell_state: player for player in player_list
        }
        self.game_over = False
        self.winner = None

    def make_move(self, player, x, y):
        """Make move by specified player.
        """
        self.game_field[x][y] = player.cell_state


    def check_game_over(self):
        """Return True, if game can't be continued
        because of win of some player or draw state.
        """
        if self.game_over:
            return True

        #check horizontal lines
        row_as_sets = [set(row) for row in self.game_field]
        for row_set in row_as_sets:
            if len(row_set) != 1:
                continue
            winner_state = tuple(row_set)[0]
            if winner_state != CELL_STATE_EMPTY:
                self.winner = self._state_to_player_map[winner_state]
                self.game_over = True
                return True


        #check vertical lines
        column_as_sets = zip(*self.game_field)
        for column_set in column_as_sets:
            if len(column_set) != 1:
                continue
            winner_state = tuple(column_set)[0]
            if winner_state != CELL_STATE_EMPTY:
                self.winner = self._state_to_player_map[winner_state]
                self.game_over = True
                return True

        #check main diagonal
        main_diagonal_set = set()
        diag_counter = 0
        for row in self.game_field:
            main_diagonal_set.add(row[diag_counter])
            diag_counter += 1

        if len(main_diagonal_set) == 1:
            winner_state = tuple(main_diagonal_set)[0]
            if winner_state != CELL_STATE_EMPTY:
                self.winner = self._state_to_player_map[winner_state]
                self.game_over = True
                return True


        #check additional diagonal
        additional_diagonal_set = set()
        diag_counter = 0
        for row in self.game_field:
            additional_diagonal_set.add(row[diag_counter])
            diag_counter += 1

        if len(additional_diagonal_set) == 1:
            winner_state = tuple(additional_diagonal_set)[0]
            if winner_state != CELL_STATE_EMPTY:
                self.winner = self._state_to_player_map[winner_state]
                self.game_over = True
                return True

        all_cells = set([cell for row in self.game_field for cell in row])
        if CELL_STATE_EMPTY not in all_cells:
            #draw is detected
            self.game_over = True
            return True


        return False


    def get_winner(self):
        return self.winner

    def as_dict(self):
        game_info = {
            "field": self.game_field.as_dict(),
            "player_list": [player.as_dict() for player in self.player_list],
            "game_over": self.game_over,
            "winner": None,
        }
        if self.winner:
            game_info["winner"] = self.winner.id

        return game_info
