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


def print_hebrew_letters():
    import unicodedata as ud
    alef = 0x05D0
    alphabet_length = 27
    for i in range(alphabet_length):
        print ud.name(unichr(alef+i))
"""        
א       ב       ג       ד       ה       ו
Alef    Bet     Gimel   Dalet   He      Vav
05D0    05D1    05D2    05D3    05D4    05D5

ז
Zayen
05D6
ח
Het
05D7
ט
Tet
05D8
י
Yod
05D9
ך
Final Kaf
05DA
כ
Kaf
05DB
ל
Lamed
05DC
ם
Final Mem
05DD
מ
Mem
05DE
ן
Final Nun
05DF
נ
Nun
05E0
ס
Samekh
05E1
ע
Ayin
05E2
ף
Final Pe
05E3
פ
Pe
05E4
ץ
Final Tsadi
05E5
צ
Tsadi
05E6
ק
Qof
05E7
ר
Resh
05E8
ש
Shin
05E9
ת
Tav
05EA"""