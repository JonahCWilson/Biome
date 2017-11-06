class PlotStatus(object):
	'''
	Rather than having one particular status, a plot can differing levels 
	of each.  The dominant attribute maintains the control, but differing
	levels allow for different actions.
	'''
	
	def __init__(self, FireLevel, WaterLevel, WindLevel, EarthLevel, Element):
		self.FireLevel = FireLevel
		self.WaterLevel = WaterLevel
		self.WindLevel = WindLevel
		self.EarthLevel = EarthLevel
		self.Element = Elements.NEUTRAL
		
	def change_element(self, element):
		self.Element = element
	
