from PlotStatus import PlotStatus

class Plot(object):
	
	def __init__(self, Position):
		self.Status = PlotStatus()
		self.Position = Position #(y, x) tuple
