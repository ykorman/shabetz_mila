# -*- coding: utf-8 -*-
from bottle import route, request, run, get, template, static_file, post, response

import server

gameStore = server.loadGameStore("sample_db.dat")

@route('/shabetz_mila')
@route('/shabetz_mila/index.html')
def main_html():
    return static_file("ui.html", root="./")

@route('/<script>.js')
def app_js(script):
    if script in ("app", "jquery.cookie", "knockout.mapping-2.4.1"):
        return static_file(script + ".js", root="./")
    else:
        abort(404, "No such script")

@route('/<stylesheet>.css')
def app_css(stylesheet):
    if stylesheet in ("bootstrap.min"):
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
        return "שגיאה כללית"

run(host='0.0.0.0', port=8181)