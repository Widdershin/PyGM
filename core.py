import pygame


class PyGM(object):
	"""Main PyGM object, handles creating shit"""
	def __init__(self, width=640, height=480, fps=60):
		super(PyGM, self).__init__()
		self.width = width
		self.height = height
		self.fps = fps
		pygame.init()
		self.screen = pygame.display.set_mode((self.width, self.height))
		self.objects = []

	def update(self):
		for obj in self.objects:
			obj.update()

	def draw(self):
		for obj in self.objects:
			obj.draw()


class PyGMObj(object):
	"""Generic PYGMObj"""
	instances = []

	def __init__(self, x, y, sprite=None):
		super(PyGMObj, self).__init__()
		self.create()
		self.x = x
		self.y = y
		self.sprite = sprite
		PyGMObj.instances.append(self)

	def create(self):
		pass

	def update(self):
		pass

	def draw(self):
		pass

	@classmethod
	def getInstances(cls, instType=None):
		"""Returns a list of all instances of type and children of type"""
		if instType is None:
			instType = cls
		return [i for i in PyGMObj.instances if isinstance(i, instType)]
