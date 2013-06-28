

class Vector2(object):
	"""Holds an XY coordinate value, and provides common operatings"""
	def __init__(self, x, y):
		super(Vector2, self).__init__()
		self.x = float(x)
		self.y = float(y)

	def __add__(self, v):
		if type(v) is not Vector2:
			raise TypeError
		else:
			return Vector2(self.x + v.x, self.y + v.y)

	def __sub__(self, v):
		if type(v) is not Vector2:
			raise TypeError
		else:
			return Vector2(self.x - v.x, self.y - v.y)

	def __mul__(self, v):
		if type(v) is not Vector2:
			v = float(v)
			return Vector2(self.x * v, self.y * v)
		else:
			return Vector2(self.x * v.x, self.y * v.y)

	def __div__(self, v):
		if type(v) is not Vector2:
			v = float(v)
			return Vector2(self.x / v, self.y / v)
		else:
			return Vector2(self.x / v.x, self.y / v.y)

	def __str__(self):
		return str((self.x, self.y,))

	def tuple(self, asInt=False):
		if asInt:
			return (int(self.x), int(self.y),)
		return (self.x, self.y,)

	def setTuple(self, tup):
		"""
		Sets the x and y coordinates from a 2d tuple
		"""
		self.x = tup[0]
		self.y = tup[1]
