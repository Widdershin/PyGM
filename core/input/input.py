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
	def keyDown(cls, key):
		"""
		Returns whether or not the specified key is currently pressed
		"""
		return KeyState.current[KeyState.keys[key]]

	@classmethod
	def keyPressed(cls, key):
		"""
		Returns whether a key was pressed in the last update
		"""
		if KeyState.current[KeyState.keys[key]] and not KeyState.previous[KeyState.keys[key]]:
			return True
		return False

	@classmethod
	def keyReleased(cls, key):
		"""
		Returns whether a key was released in the last update
		"""
		if not KeyState.current[KeyState.keys[key]] and KeyState.previous[KeyState.keys[key]]:
			return True
		return False
