# -*- coding: utf-8 -*-
from bottle import route, request, run, get, template, static_file, post, response
import json
import server

gameStore = server.loadGameStore("sample_db.dat")

@route('/shabetz_mila')
@route('/shabetz_mila/index.html')
def main_html():
    return static_file("app.html", root="./")

@route('/<script>.js')
def app_js(script):
    if script in ("app", "jquery.cookie", "knockout.mapping-2.4.1"):
        return static_file(script + ".js", root="./")
    else:
        abort(404, "No such script")

@route('/<stylesheet>.css')
def app_css(stylesheet):
    if stylesheet in ("bootstrap.min", "app"):
        return static_file(stylesheet + ".css", root="./")
    else:
        abort(404, "no such stylesheet")
   
@post('/shabetz_mila/login')
def login():
    name     = request.forms.get('username')
    password = request.forms.get('password')
    player = gameStore.players.findPlayer(name)
    if (player is None) or (player.password != password):
        return "failure"
    else:
        response.set_cookie("username", player.name)
        return "success"

@post('/shabetz_mila/start_game')
def start_game():
    playerName = request.forms.get('player_name')
    rivalName = request.forms.get('rival_name')
    player = gameStore.players.findPlayer(playerName)
    rival = gameStore.players.findPlayer(rivalName)
    if (player is not None) and (rival is not None):
        game = server.Game(player.name, rival.name)
        gameStore.games.addGame(game)
        return game.toJson()
    else:
        return '{"status": -2}'

@post('/shabetz_mila/submit_word')
def submit_word():
    gameId = int(request.forms.get('id'))
    playerName = request.forms.get('player_name')
    rivalName = request.forms.get('rival_name')
    word = json.loads(request.forms.get('word'))
    letterList = []
    for letter in word:
        letterList.append(letter[u'index']-1)
    game = gameStore.games.getGame(gameId)
    if (game == None):
        return '{"status": -1}'
    game.tryPlayTurn(playerName, letterList)
    return game.toJson()

def convertToExistingGamesJson(playerName, gameList):
    json = '{ "games": [ '
    for game in gameList:
        json += '{ "id": ' + str(game.id) + ','
	json += '"played_against": "' + (game.rival_id if (game.player_id == playerName) else game.player_id) + '", '
	json += '"last_turn": "' + game.lastTurnOn.strftime("%m-%d %H:%M") + '" }'
    json += ' ] }'
    return json

@post('/shabetz_mila/get_gamelist')
def get_gamelist():
    playerName = request.forms.get('player_name')
    player = gameStore.players.findPlayer(playerName)
    if (player is None):
        return '{"status": -1}'
    gameList = gameStore.games.getGamesByPlayer(player.name)
    gameListJson = convertToExistingGamesJson(playerName, gameList)
    return gameListJson

@post('/shabetz_mila/get_game_by_id')
def get_game_by_id():
    gameId = request.forms.get('game_id')
    game = gameStore.games.getGame(gameId)
    if (game is None):
        return '{"status": -1}'
    return game.toJson()

run(host='0.0.0.0', port=8181)
