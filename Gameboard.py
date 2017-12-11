from Plot import Plot

class Gameboard(object):
	
	def __init__(self):
		self.grid = self.populate()
		self.initialize()
	
	def populate(self):
		output = {}
		for i in range(10):
			for j in range(10):
				output[(i, j)] = Plot((i, j))
		return output
		
	def initialize(self);
		pass
