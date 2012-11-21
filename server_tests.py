import unittest
import server_side

class TestPlayerGet(unittest.TestCase):
    def testSimplePlayerGet(self):
        p = server_side.get_player("player_name");
        self.assertEqual("player_name", p.name);
    
if __name__ == '__main__':
    unittest.main()