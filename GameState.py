class GameState(object):
	
	def __init__(self):
		self.Board = Gameboard()
		self.Players = self.initialize_players()
		
	
	
	def initialize_players(self):
		positions = [(0, 0), (0, 3), (0, 6), (0, 9), 
			(9, 0), (9, 3), (9, 6), (9, 9)]
		
		Players = []
		for pos in positions:
			Players.append(new Player(pos, 10, 10, 10, 10, None))
		return Players
