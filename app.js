(function() {

	$.mobile.ignoreContentEnabled = true;

	$("#loginBtn").click(function() {
		username = $("#username").val();
		password = $("#password").val();
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
		player_name = $.cookie("username");
		rival_name = $("#rivalName").val();
		$.post("shabetz_mila/start_game",
			{ player_name: player_name, rival_name: rival_name },
			function(response) {
				appViewModel.updateFromServer(response);
				$.mobile.changePage($("#game"));
			});
	});

	function Cell(index, letter) {
		var self = this;
		self.index = index;
		self.letter = ko.observable(letter);
		self.selected = ko.observable(false);
	}

	function AppViewModel() {
		var self = this; // KO convention	
		var i;

		self.cells = ko.observableArray();

		// create 25 observable cells
		for (i=1; i <= 25; i++) {
			self.cells.push(new Cell(i,(i<10) ? "0" + String(i) : String(i)));
		}

		self.selected = ko.observableArray();

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
			var i;
			for (i=0; i < 25; i++) {
				self.cells()[i].letter(game.letterList[i]);
			}
		};

	}

	appViewModel = new AppViewModel();
	ko.applyBindings(appViewModel);

})();