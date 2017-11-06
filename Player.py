class Player(object):

	'''
	Player: abstract
	Pos: (x, y)
	HP: integer
	PP: integer
	XP: integer
	MV: integer
	Spells: list
	'''
	
	def init(self, Pos, HP, PP, XP, MV, Spells):
		self.Pos = Pos
		self.HP = HP
		self.PP = PP
		self.XP = XP
		self.MV = MV
		self.Spells = Spells
		

