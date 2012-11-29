Shabetz-Mila
===============

Online word puzzle game in Hebrew for 2 players.

# Screens
----------

## Main Screen
* Start new game
* List of current games
* List of old games
* Settings

## Game Screen
* Header: player scores
* Body: word to play, letter matrix.
* Footer: actions

	### Actions
	* Return to menu
	* Pass
	* Submit Word
	* Show played words
	* Reset matrix
	
## New Game Screen
* Select opponent from:
	1. List of recent opponents
	2. Enter opponent name
	3. Random opponent
* Start game

# Database
----------

## Players Table
* Player name
* Player id
* Player games

## Games Table
* Game id
* Letters list
* Player A id
* Player B id
* Player A letter indexes
* Player B letter indexes
* Player A played words
* Player B played words

## Database actions:
* Create player
* Create game
* Play turn
* Get player
* Get game

TODO
====
* Use Apple specific "Web Clip" API to create an icon for the game and other stuff (See http://tinyurl.com/7384jyk)
*

IDEAS
=====
* Build a list of letter occurrences based on Scrabble values (a list of 27 integers).
* To generate random letters based on occurrence, we generate a list of letters based on the following algorithm:
	MAX_OCC = 10
	for l in occ_list:
		for c in range(l):
			letter_list.append(MAX_OCC - letters[l])
	Then we get random values from the letter_list.
* If we decide not to use "final" letters, then their occurrence should be MAX_OCC.
* I need a database schema. It needs to have a table for configurations and hold a row for version of the schema.
* The version row should always be written last so that if the db transaction fails it will be easy to recognize.
* When opening the database file I need to check for the version.
* The bottle microframework has a sqlite plugin, I should use it