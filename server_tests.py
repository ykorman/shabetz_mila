import sys

import unittest
import server_side

class TestPlayerGet(unittest.TestCase):
    def testSimplePlayerGet(self):
        p = server_side.get_player("player_name")
        self.assertEqual("player_name", p.name)
        p1 = server_side.get_player("player2")
        self.assertEqual("player2", p1.name)
        self.assertEqual("player_name", p.name)
        
class TestStorage(unittest.TestCase):
    def testStorageOpen(self):
        storage = server_side.open_storage("storage_name")
        self.assertEqual(storage.get_name(), "storage_name")
    
if __name__ == '__main__':
    unittest.main()
    