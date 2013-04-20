﻿import sys
import unittest
import json

import server
import hspell

class TestPlayer(unittest.TestCase):
    def testPlayerConstructor(self):
        p = server.Player("aaa", "bbb", "ccc")
        self.assertEqual(p.name, "aaa")
        self.assertEqual(p.password, "bbb")
        self.assertEqual(p.email, "ccc")
        
class TestPlayerList(unittest.TestCase):
    def setUp(self):
        self.pl = server.PlayerList()
    
    def testPlayerListConstructor(self):
        self.assertNotEqual(self.pl, None)
        
    def testPlayerListAddPlayer(self):
        p = server.Player("aaa", "bbb", "ccc")
        self.pl.addPlayer(p)
        self.assertEqual(self.pl.list[0].name, "aaa")
    
    def testPlayerListGetPlayer(self):
        p = server.Player("aaa", "bbb", "ccc")
        self.pl.addPlayer(p)
        pf = self.pl.findPlayer("aaa")
        pn = self.pl.findPlayer("bbb")
        self.assertEqual(pf.name, "aaa")
        self.assertEqual(pn, None)
        
class TestGame(unittest.TestCase):
    def testGameConstructor(self):
        p1 = server.Player("aaa", "bbb", "ccc")
        p2 = server.Player("zzz", "yyy", "xxx")
        g = server.Game(p1.name,p2.name)
        self.assertNotEqual(g.id, 0)
        self.assertEqual(len(g.letters), 25)
        
class TestGameList(unittest.TestCase):
    def TestGameListGetGame(self):
        p1 = server.Player("aaa", "bbb", "ccc")
        p2 = server.Player("zzz", "yyy", "xxx")
        g = server.Game(p1.name,p2.name)
        gl = server.GameList()
        gl.addGame(g)
        self.assertEqual(gl.getGame(g.id), g.id)
    
class TestGameStore(unittest.TestCase):
    def testGameStoreLoadNSave(self):
        gs = server.GameStore()
        p1 = server.Player("aaa", "bbb", "ccc")
        p2 = server.Player("zzz", "yyy", "xxx")
        g = server.Game(p1.name,p2.name)
        gs.players.addPlayer(p1)
        gs.players.addPlayer(p2)
        gs.games.addGame(g)
        gs.save("test_db.dat")
        gs1 = server.loadGameStore("test_db.dat")
        self.assertNotEqual(gs1.games.getGame(g.id),None)
        
class TestGameSerializeToJson(unittest.TestCase):
    def testSerializeToJson(self):
        p1 = server.Player("aaa", "bbb", "ccc")
        p2 = server.Player("zzz", "yyy", "xxx")
        g = server.Game(p1.name,p2.name)
        #g.toJson()

class TestHspell(unittest.TestCase):
    def testHspellInit(self):
        h = hspell()

    def testHspellWordCheck(self):
        h = hspell()
        self.assertEqual(h.checkWord(u'שלום'), True)
        self.assertEqual(h.checkWord(u'לושם'), False)
        
if __name__ == '__main__':
    unittest.main()
    