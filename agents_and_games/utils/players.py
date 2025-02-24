"""
An enumeration for player tokens in a game.
"""

from enum import Enum


class Players(Enum):
    """
    An enumeration for player tokens in a game.

    Attributes:
        P1 (str): Token for Player 1 ('X').
        P2 (str): Token for Player 2 ('O').
        EMPTY (str): Token for an empty cell (' ').
        MAP (dict): A mapping of player tokens to integers.
    """
    P1 = "X"
    P2 = "O"
    EMPTY = " "
    MAP = {    
        P1: 1,
        P2: -1,
        EMPTY: 0,
    }
