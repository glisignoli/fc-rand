from typing import Dict

class Genres:
    def __init__(self):
        self.genres = {}

        self._add_genres()

    def _add_genres(self):
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

        for g in self.genres.keys():
            # Remove any duplicate gids from the genres
            self.genres[g] = list(set(self.genres[g]))

    def validate_genres(self, game_ids):
        # Remove any gids from self.generes that aren't in game_ids

        for genre in self.genres.keys():
            prune_list = []
            for gid in self.genres[genre]:
                if gid not in game_ids:
                    prune_list.append(gid)

            for gid in list(set(prune_list)):
                self.genres[genre].remove(gid)


        # Remove generes that don't have any game_ids in them:
        prune_list = []

        for genre in self.genres.keys():
            if len(self.genres[genre]) == 0:
                prune_list.append(genre)

        for genre in prune_list:
            del self.genres[genre]
