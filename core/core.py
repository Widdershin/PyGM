import pygame
from sprite import Sprite


class PyGM(object):
	"""Main PyGM object, handles creating shit"""
	objects = []
	screen = None

	def __init__(self, width=640, height=480, fps=60):
		super(PyGM, self).__init__()
		self.width = width
		self.height = height
		self.fps = fps
		self.clock = pygame.time.Clock()
		pygame.init()
		PyGM.screen = pygame.display.set_mode((self.width, self.height))

	def update(self):
		for obj in self.objects:
			obj.update()

	def draw(self):
		PyGM.screen.fill((0, 0, 0))
		for obj in self.objects:
			obj.draw()
		pygame.display.flip()
		self.clock.tick(self.fps)


class PyGMObj(object):
	"""Generic PYGMObj"""
	instances = []

	def __init__(self, x, y, sprite=None):
		super(PyGMObj, self).__init__()
		self.create()
		self.x = x
		self.y = y
		self.sprite = Sprite(sprite, PyGM.screen)
		PyGM.objects.append(self)

	def create(self):
		pass

	def update(self):
		pass

	def draw(self):
		if self.sprite is not None:
			self.sprite.draw(self.x, self.y)

	@classmethod
	def getInstances(cls):
		"""Returns a list of all instances of type and children of type"""
		return [i for i in PyGM.objects if isinstance(i, cls)]
