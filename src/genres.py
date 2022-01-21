from typing import Dict

class Genres:
    def __init__(self):
        self.genres = {}

        self.add_genres()

    def add_genres(self):
        # Open genre.ini, and create a dictionary of genres/games
        # Genres looks like this:
        # [Ball & Paddle]
        # ark1ball
        # arkangc
        # 
        # [Genre 2]
        # gameid2
        # somegame3

        with open('src/catver/genre.ini', 'r') as f:
            for line in f:
                if line.startswith('['):
                    # If a line starts with a [, it's a new genre
                    # Create a new key in the dictionary
                    # The key is the genre name
                    # The value is a list of games in that genre
                    # The list is empty
                    genre = line.strip('[]\n')
                    self.genres[genre] = []

                elif line.strip() != "":
                    # If the line doesn't start with a [, it's a game
                    # Add the game to the list of games for the current genre
                    self.genres[genre].append(line.strip('\n'))

                else:
                    continue
