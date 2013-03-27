(function() {

	$.mobile.ignoreContentEnabled = true;

	$("#loginBtn").click(function() {
		var username = $("#username").val();
		var password = $("#password").val();
		$.post("shabetz_mila/login",
			{ username: username, password: password },
			function(response) {
				if (response == "success") {
					$.mobile.changePage($("#main"));
					// alert($.cookie("username"));
				} else
				$("#loginError").popup("open");		
			});
	});
	
	$("#startGame").click(function() {
		var player_name = $.cookie("username");
		var rival_name = $("#rivalName").val();
		$.post("shabetz_mila/start_game",
			{ player_name: player_name, rival_name: rival_name },
			function(response) {
				appViewModel.updateFromServer(response);
				$.mobile.changePage($("#game"));
			});
	});

	$("#submitWord").click(function() {
		var player_name = appViewModel.aPlayer.name();
		var rival_name = appViewModel.bPlayer.name();
		var word = ko.mapping.toJS(appViewModel.selected);
		console.log(word);
		$.post("shabetz_mila/submit_word",
			{ "player_name": player_name, "rival_name": rival_name, "word": JSON.stringify(word) },
			function(response) {
				
			});
	});

	function Cell(index, letter) {
		var self = this;
		self.index = index;
		self.letter = ko.observable(letter);
		self.selected = ko.observable(false);
	};

	function Player(name, score) {
		var self = this;
		self.name = ko.observable(name);
		self.score = ko.observable(score);
	};

	function AppViewModel() {
		var self = this; // KO convention	
		var i;

		self.cells = ko.observableArray();

		// create 25 observable cells
		for (i=1; i <= 25; i++) {
			self.cells.push(new Cell(i,(i<10) ? "0" + String(i) : String(i)));
		}

		self.selected = ko.observableArray();

		self.aPlayer = new Player("",0);
		self.bPlayer = new Player("",0);

		self.select = function(cell) {
			if (cell.selected()) {
				cell.selected(false);
				self.selected.remove(cell);
			} else { 
				cell.selected(true);
				self.selected.push(cell);
			}
		};

		self.updateFromServer = function(data) {
			var game = jQuery.parseJSON(data);
			self.aPlayer.name(game.aPlayer);
			self.aPlayer.score(game.aWords.length);
			self.bPlayer.name(game.bPlayer);
			self.bPlayer.score(game.bWords.length);
			var i;
			for (i=0; i < 25; i++) {
				self.cells()[i].letter(game.letterList[i]);
			}
		};

	}

	appViewModel = new AppViewModel();
	ko.applyBindings(appViewModel);

})();