from PlotStatus import PlotStatus

class Plot(object):
	
	def __init__(self, Position):
		self.__Status = PlotStatus(0)
		self.__Position = Position #(y, x) tuple
		
	def get_status():
		return self.__Status
	
	def get_position():
		return self.__Position
		
		
	
