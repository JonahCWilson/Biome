class GameBoard(dict):
	
	def init(self):
		self.populate()
	
	def populate(self):
		for i in range(10):
			for j in range(10):
				self[(i,j)] = Plot()
