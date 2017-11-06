import Elements

class PlotStatus(object):
	'''
	Rather than having one particular status, a plot can differing levels 
	of each.  The dominant attribute maintains the control, but differing
	levels allow for different actions.
	'''
	
	def __init__(self, FireLevel, WaterLevel, WindLevel, EarthLevel, Element):
		self.__FireLevel = FireLevel
		self.__WaterLevel = WaterLevel
		self.__WindLevel = WindLevel
		self.__EarthLevel = EarthLevel
		self.__Element = Elements.NEUTRAL
		
	def set_element(self, element):
		self.__Element = element
		
	def get_element(self):
		return self.__Element
		
	
	
