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

}

ko.applyBindings(new AppViewModel());