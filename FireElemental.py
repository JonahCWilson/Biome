from Character import Character

class FireElemental(Character):

    def __init__(self, x, y):
	super(FireElemental, self).__init__(10, 10, 10)
	self.x_coord = x
	self.y_coord = y


