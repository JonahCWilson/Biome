class GameState(object):
	
	def __init__(self):
		self.Board = GameBoard()
		self.Player = Player()
		
class GameBoard(dict):
	
	def __init__(self):
		self.populate()
	
	def populate(self):
		for i in range(10):
			for j in range(10):
				self[(i,j)] = Plot()
	
	
class Plot(object):
	
	def __init__(self):
		self.status = PlotStatus.NEUTRAL
		
class Player(object):
	
	def __init__(self):
		self.pos = (5, 5)
		
	# Player will be an abstract class
	# Each elemental will have different base movement, hp, mp, etc.
	# Movement functions should be unique to each elemental

		
class PlotStatus(object):
	NEUTRAL = 0
	FIRE = 1
	WATER = 2
	WIND = 3
	EARTH = 4
	
