import server

gs = server.GameStore()
p1 = server.Player("aaa", "bbb", "ccc")
p2 = server.Player("zzz", "yyy", "xxx")
g = server.Game(p1.name,p2.name)
gs.players.addPlayer(p1)
gs.players.addPlayer(p2)
gs.games.addGame(g)
gs.save("sample_db.dat")