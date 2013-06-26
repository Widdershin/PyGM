"""
Handles all input
"""
import pygame.key
import core.input.keys


class KeyState(object):
	"""Stores the current and previous state of the keys"""
	def __init__(self):
		super(KeyState, self).__init__()
		self.update()
		self.endUpdate()
		self.keys = core.input.keys.createKeys()

	def update(self):
		"""
		Updates the Key State
		"""
		self.current = pygame.key.get_pressed()

	def endUpdate(self):
		"""
		Sets the previous key state to the current key state, only use at the end
		"""
		self.previous = self.current

	def isKeyDown(self, key):
		"""
		Returns whether or not the specified key is currently pressed
		"""
		return self.current[self.keys[key]]
