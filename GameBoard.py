from Plot import *

class GameBoard(object):

	def __init__(self, size):
	    self.size = size
	    self.grid = {}
	    self.initialize()

	def print_board(self):
		for row in self.grid:
			for plot in row:
				print plot.print_plot()


	def initialize():
		for i in range(self.size):
			for j in range(self.size):
				self.grid[(i, j)] = Plot(i, j)

