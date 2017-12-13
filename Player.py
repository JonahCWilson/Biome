from abc import ABCMeta

class Player(object):

	__metaclass__ = ABCMeta
	'''
	Player: abstract
	Pos: (x, y)
	HP: integer
	PP: integer
	XP: integer
	MV: integer
	Spells: list
	'''
	
		
	def __init__(self, Position, HitPoints, PowerPoints, ExperiencePoints, MoveCount, Spells):
		self.__Position = Position
		self.__HitPoints = HitPoints
		self.__PowerPoints = PowerPoints
		self.__ExperiencePoints = ExperiencePoints
		self.__MoveCount = MoveCount
		self.__Spells = Spells
		super().__init__()
		
		
	def get_position(self):
		return self.__Position
	
	def set_position(self, p):
		self.__Position = p
	
	def get_hitpoints(self):
		return self.__HitPoints
		
	def set_hitpoints(self, hp):
		self.__HitPoints = hp
		
	def get_powerpoints(self):
		return self.__PowerPoints
		
	def set_powerpoints(self, pp):
		self.__PowerPoints = pp
		
	def get_experiencepoints(self):
		return self.__ExperiencePoints
		
	def set_experiencepoints(self, xp):
		self.__ExperiencePoints = xp
	
	def get_movecount(self):
		return self.__MoveCount
	
	def set_movecount(self, moves):
		self.__MoveCount = moves
		
	def get_spells(self):
		return self.__Spells
	
	def set_spells(self, spells):
		self.__Spells = spells
	
	def move(self):
		pass
		

