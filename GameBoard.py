from Tile import *
from TileStatus import *

class GameBoard(object):

	def __init__(self, size):
	    self.size = size
	    self.grid = {}
	    self.initialize()
	
	def initialize(self):
		for i in range(self.size):
			for j in range(self.size):
				self.grid[(i, j)] = Tile(j, i, TileStatus.NEUTRAL)


