class Game:

    def __init__(self, name, players=[]):

        self.name    = name
        self.players = players

    def add_player(self, player):
        self.players.append(player)

    def remove_player(self, player):
        self.players.remove(player)

    def describe(self):
        print("{} game.".format(self.name))
        print("{} players in game:".format(len(self.players)))
        for player in self.players:
            print(player)

class Player:

    def __init__(self, name):

        self.name = name

    def describe(self):
        print("I am", self.name)

    def __repr__(self):
        return "Player <{}>".format(self.name)


