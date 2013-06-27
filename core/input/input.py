"""
Handles all input
"""
import pygame.key
import core.input.keys


class Keys(object):
	current = None
	previous = None
	keys = {}
	"""Stores the current and previous state of the keys"""
	def __init__(self):
		super(Keys, self).__init__()
		self.update()
		self.endUpdate()
		Keys.keys = core.input.keys.createKeys()

	def update(self):
		"""
		Updates the Key State
		"""
		Keys.current = pygame.key.get_pressed()

	def endUpdate(self):
		"""
		Sets the previous key state to the current key state, only use at the end
		"""
		Keys.previous = Keys.current

	@classmethod
	def keyDown(cls, key):
		"""
		Returns whether or not the specified key is currently pressed
		"""
		return Keys.current[Keys.keys[key]]

	@classmethod
	def keyPressed(cls, key):
		"""
		Returns whether a key was pressed in the last update
		"""
		if Keys.current[Keys.keys[key]] and not Keys.previous[Keys.keys[key]]:
			return True
		return False

	@classmethod
	def keyReleased(cls, key):
		"""
		Returns whether a key was released in the last update
		"""
		if not Keys.current[Keys.keys[key]] and Keys.previous[Keys.keys[key]]:
			return True
		return False
