import random
import cPickle
import json
import unicodedata as ud

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
        if (self.aPlayer == player):
            self.aWords.append(word)
        elif (self.bPlayer == player):
            self.bWords.append(word)
            
    def genLetterList(self):
        l = []
        alphabet_length = 27
        alef = 0x05D0
        good_letters = [0,1,2,3,4,5,6,7,8,9,
                        #10,
                        11,12,
                        #13,
                        14,
                        #15,
                        16,17,18,
                        #19,
                        20,
                        #21,
                        22,23,24,25,26]
        list_size = 25
        for i in range(list_size):
            index = random.randint(0, len(good_letters) - 1)
            letter = unichr(alef + good_letters[index])
            l.append(letter)
            # print str(i) + ":" + str(index) + "=" + ud.name(letter)
        return l
        
    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)    
        
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
        