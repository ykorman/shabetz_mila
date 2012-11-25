import sqlite3

def get_player(name):
    return Player(name);
    
def open_storage(name):
    return Storage(name)

class Player:   
    def __init__(self, name=""):
        self.name = name

    def name(self):
        return self.name
        
class Storage:
    def __init__(self, name=":memory:"):
        self.name = name
        self.conn = sqlite3.connect(self.name)
        
    def __del__(self):
        self.conn.close()
        
    def get_name(self):
        return self.name