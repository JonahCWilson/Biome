from Elements import Elements

class PlotStatus(object):
	'''
	Currently, a status can have a single type, and a strength of that 		type.
	
	Future Update:
	Rather than having one particular status, a plot can differing levels 
	of each.  The dominant attribute maintains the control, but differing
	levels allow for different actions.
	'''
	
	def __init__(self, level):
		self.__Element = Elements.NEUTRAL
		self.__Level = level
		
	def set_element(self, element):
		self.__Element = element
		
	def get_element(self):
		return self.__Element
		
	def set_level(self, level):
		self.__Level = level
	
	def get_level(self);
		return self.__Level
	
	def increment_level(self):
		if self.__Level < 5:
			self.__Level += 1
	
	def decrement_level(self):
		if self.__Level > 0:
			self.__Level -= 1
			
	
	
