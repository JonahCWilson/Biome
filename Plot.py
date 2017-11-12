from PlotStatus import PlotStatus

class Plot(object):
	
	def __init__(self, Position):
		self.Status = PlotStatus(0, 0, 0, 0)
		self.Position = Position #(y, x) tuple
