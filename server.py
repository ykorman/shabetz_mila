import random
import cPickle
import json
import unicodedata as ud
import hspell
from datetime import datetime

spell = hspell.Hspell()

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
        
SM_GAME_STATUS_GOOD = 0
SM_GAME_STATUS_WRONG_TURN = 1
SM_GAME_STATUS_BAD_WORD = 2

class Game:
    def __init__(self, player_id, rival_id, letters=None):
        self.id = random.getrandbits(32)
        self.player_id = player_id
        self.rival_id = rival_id
        if (letters != None):
            self.letters = letters
        else:
            self.letters = self.genletters()
        self.playerLetters = []
        self.rivalLetters = []
        self.whosTurn = player_id
        self.status = SM_GAME_STATUS_GOOD
	self.createdOn = datetime.utcnow()
	self.lastTurnOn = self.createdOn

    def constructWord(self, letterList):
        word = ''
        for index in letterList:
            word += self.letters[index]
        return word

    def checkWord(self, word):
        return spell.check_word(word)
        
    def tryPlayTurn(self, player_id, letterList):
        if (self.whosTurn != player_id):
            self.status = SM_GAME_STATUS_WRONG_TURN
            return False
        word = self.constructWord(letterList)
        if self.checkWord(word):
            self.updateGame(player_id, letterList)
            self.status = SM_GAME_STATUS_GOOD
            return True
        else:
            self.status = SM_GAME_STATUS_BAD_WORD
            return False

    def updateGame(self, player_id, letterList):
        self.lastTurnOn = datetime.utcnow()
        if (self.player_id == player_id):
            self.playerLetters = letterList
            self.whosTurn = self.rival_id     
        else:
            self.rivalLetters = letterList
            self.whosTurn = self.player_id
            
    def genletters(self):
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

    def getGamesByPlayer(self, player_id):
        player_games_list = []
        for game in self.list:
            if ( (game.player_id == player_id) or
                 (game.rival_id == player_id) ):
                player_games_list.append(game)
        return player_games_list

class GameStore:
    def __init__(self, db_name = None):
        self.games = GameList()
        self.players = PlayerList()
        self.db_name = db_name
        
    def save(self, name = None):
        if (name != None):
            self.db_name = name
        f = open(self.db_name, "w")
        cPickle.dump(self,f)

    def __del__(self):
        self.save()
        
def loadGameStore(name="default_db.dat"):
    f = open(name, "r")
    gs = cPickle.load(f)
    gs.db_name = name
    return gs
        
