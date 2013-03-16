(function() {
	'use strict';
	
	var testList = [
		{ index: 1, value: 'A'},
		{ index: 2, value: 'B'},
		{ index: 3, value: 'C'},
		{ index: 4, value: 'D'},
		{ index: 5, value: 'E'},
	];
	
	function Letter(value, index) {
		self = this;
		self.value = value;
		self.index = index;
	}
	
	function ViewModel() {
		self = this;
		
		self.upperList = ko.observableArray();
		self.lowerList = ko.observableArray();
		
		// populate list
		testList.forEach(function(element, index, array) {
			self.lowerList.push(element);
		});
		
		self.move = function(letter) {
			// find in which list the letter is right now
			// remove it from the list
			// add it to the other list in the right place
			if (self.lowerList.indexOf(letter) != -1) {
				// in lowerList
				self.lowerList.remove(letter);
				self.upperList.splice(letter.index-1,0,letter);
			} else {
				// in upperList
				self.upperList.remove(letter);
				self.lowerList.splice(letter.index-1,0,letter);
			}
			
		};
		

		
	}
	
			$.getJSON("localhost:8081/shabetz_mila/start_game", 
		{ player_name: "aaa", rival_name: "zzz" } 
		,function(game) {
			self.gameId = game.id;
			self.letterList = game.letterList;
			alert(self.letterList);
		});
	
	ko.applyBindings(new ViewModel());
}());