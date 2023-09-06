# Title: Basic Soccer Penalty Shoot-Out Game
# Author: Brooke Anderson
# Description: A basic soccer penalty shoot-out game programmed in Python


class InvalidPlayerError(Exception):
    """user-defined exception to a player not listed on the team"""
    pass


class CreateGame:
    """a class to create the game"""
    pass


class CreatePlayers:
    """a class to create/update the players"""
    def __init__(self, player_name):
        self._player_name = player_name

    def get_name(self):
        """returns the players name"""
        return self._player_name


class PlayGame:
    """a class to update and play the game"""
    pass
