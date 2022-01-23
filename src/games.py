import glob
import json

class Games:
    def __init__(self):
        self.games = {}

        self._add_games()
        self._valid_games()

    def _add_games(self):
        # Read src/gamenames.txt and create a dictionary of gameids/gamenames.
        # gamenames.txt looks like this:
        # 005               "005"
        # 100lions          "100 Lions (10219211, NSW/ACT)"
        # 10yard            "10-Yard Fight (World, set 1)"
        # 10yard85          "10-Yard Fight '85 (US, Taito license)"

        with open('src/catver/gamenames.txt', 'r') as f:
            for line in f:
                # Split the line into a list of strings
                # The first string is the gameid
                # The second string is the gamename
                gameid, gamename = line.split('"')[:2]

                # Remove the newline character from the gamename
                gamename = gamename.strip('\n')

                # Add the gameid and gamename to the dictionary
                self.games[gameid.strip()] = gamename.strip()

    def _valid_games(self):
        with open('src/catver/fc_games.json') as f:
            fc_games = json.load(f)['games']

        prune_list = []
        valid_games = []

        for gid in self.games.keys():
            if gid not in fc_games:
                # Remove from self.games
                prune_list.append(gid)
            else:
                valid_games.append(gid)

        for gid in prune_list:
            del self.games[gid]
