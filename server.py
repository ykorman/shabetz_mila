import random
import cPickle

class Player:
    def __init__(self, name, password, email):
        self.name = name
        self.password = password
        self.email = email
        
class PlayerList:
    def __init__(self):
        self.list = []
        
    def addPlayer(self, player):
        self.list.append(player);
        
    def findPlayer(self, name):
        for player in self.list:
            if (player.name == name):
                return player
        return None
        
class Game:
    def __init__(self, aplayer, bplayer):
        self.id = random.getrandbits(32)
        self.aPlayer = aplayer
        self.bPlayer = bplayer
        self.letterList = self.genLetterList()
        self.aWords = []
        self.bWords = []
        
    def playWord(self, player, word):
        if (self.aPlayer.name == player.name):
            self.aWords.append(word)
        elif (self.bPlayer.name == player.name):
            self.bWords.append(word)
            
    def genLetterList(self):
        l = []
        for i in range(25):
            l.append(random.randint(0,27))
        return l
    
class GameList:
    def __init__(self):
        self.list = []
        
    def addGame(self, game):
        self.list.append(game)
        
    def getGame(self, id):
        for game in self.list:
            if (game.id == id):
                return game
        return None

class GameStore:
    def __init__(self):
        self.games = GameList()
        self.players = PlayerList()
        
    def save(self, name):
        f = open(name, "w")
        cPickle.dump(self,f)
        
def loadGameStore(name):
    f = open(name, "r")
    return cPickle.load(f)
        