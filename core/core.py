import sys
import pygame
from sprite import Sprite
import input


class PyGM(object):
	"""Main PyGM object, handles creating shit"""
	objects = []
	keys = None
	screen = None

	def __init__(self, width=640, height=480, fps=60):
		super(PyGM, self).__init__()
		self.width = width
		self.height = height
		self.fps = fps
		self.clock = pygame.time.Clock()
		pygame.init()
		PyGM.screen = pygame.display.set_mode((self.width, self.height))
		PyGM.keys = input.Keys()
		PyGM.mouse = input.Mouse()

	def update(self):
		"""
		Main update loop for the game engine
		"""
		pygame.event.pump()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()  # Quit the game if the exit button is pressed

		self.keys.update()
		self.mouse.update()

		for obj in PyGM.objects:
			obj.update()  # Run the update loop

		self.keys.endUpdate()
		self.mouse.endUpdate()

	def draw(self):
		"""
		Draw loop for the game engine
		"""

		PyGM.screen.fill((0, 0, 0))  # Clear the screen to black, should add BGCOLOR

		for obj in self.objects:
			obj.draw()  # Run the draw event of all objects

		pygame.display.flip()  # Print to the screen
		self.clock.tick(self.fps)


class PyGMObj(object):
	"""Generic PYGMObj"""
	instances = []

	def __init__(self, x, y, sprite=None):
		super(PyGMObj, self).__init__()
		self.create()
		self.x = x
		self.y = y
		if sprite is not None:
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
	def instances(cls):
		"""Returns a list of all instances of type and children of type"""
		return [i for i in PyGM.objects if isinstance(i, cls)]
