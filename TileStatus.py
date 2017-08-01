class TileStatus(object):

# There are 5 possible statuses
# 0: Neutral, unclaimed
# 1: Fire
# 2: Water
# 3: Wind
# 4: Earth
#
# 1-4 may also have up to three levels of strength which will all go into
# changing a character's attributes.

    def __init__(self, status, level):
		self.status = status
		self.level = level

    # void
    def Increment_Level(self):
		if self.level < 3:
	    	self.level += 1

	# void
    def Decrement_Level(self):
		if self.level > 0:
	    	self.level -= 1
		else:
	    	self.level = 0
	    	self.status = 0

	# void
	def Change_Status(n):
		self.status = n


