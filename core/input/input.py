"""
Handles all input
"""
import pygame.key
import core.input.keys


class KeyState(object):
	current = None
	previous = None
	keys = {}
	"""Stores the current and previous state of the keys"""
	def __init__(self):
		super(KeyState, self).__init__()
		self.update()
		self.endUpdate()
		KeyState.keys = core.input.keys.createKeys()

	def update(self):
		"""
		Updates the Key State
		"""
		KeyState.current = pygame.key.get_pressed()

	def endUpdate(self):
		"""
		Sets the previous key state to the current key state, only use at the end
		"""
		KeyState.previous = KeyState.current

	@classmethod
	def isKeyDown(cls, key):
		"""
		Returns whether or not the specified key is currently pressed
		"""
		return KeyState.current[KeyState.keys[key]]
