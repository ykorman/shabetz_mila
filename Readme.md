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