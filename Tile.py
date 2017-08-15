class Tile(object):

	def __init__(self, row, col, status):
		self.status = status
		self.row = row
		self.col = col

	def change_status(self, newStatus):
		self.status = newStatus
