class Character(object):

	def __init__(self, hitpoints, magicpoints, range):
		self.HP = hitpoints
		self.MP = magicpoints
		self.RANGE = range

	def Get_HP(self):
		return self.HP

	def Get_MP(self):
		return self.MP

	def Get_Range(self):
		return self.RANGE
