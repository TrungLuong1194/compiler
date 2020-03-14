class TransitionsClosures:
	def __init__(self, start):
		self.start = start
		self.closure = []

	def addValue(self, value):
		self.closure.append(value)

	def getClosure(self):
		return self.closure

	def display(self):
		print('q' + str(self.start) + ' = q' + str(sorted(self.closure)))
