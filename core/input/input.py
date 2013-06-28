"""
Handles all input
"""
import pygame.key
import pygame.mouse
import core.input.keys
import core.maths as maths


class Keys(object):
	"""Stores the current and previous state of the keys"""

	current = None
	previous = None
	keys = {}

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


class Mouse(object):
	"""Stores the state of the mouse"""

	current = None
	previous = None
	position = maths.Vector2(0, 0)
	buttons = {}

	def __init__(self):
		super(Mouse, self).__init__()
		self.update()
		self.endUpdate()
		Mouse.buttons = core.input.keys.createMB()

	def update(self):
		"""
		Updates the mouse state
		"""
		Mouse.current = pygame.mouse.get_pressed()
		Mouse.position.setTuple(pygame.mouse.get_pos())

	def endUpdate(self):
		"""
		Sets the previous state to the current state
		"""
		Mouse.previous = Mouse.current

	@classmethod
	def buttonDown(cls, button):
		"""
		Takes a string of the mouse button, returns whether it is down
		"""

		return Mouse.current[Mouse.buttons[button]]

	@classmethod
	def buttonPressed(cls, button):
		"""
		Returns whether a button was pressed in the last update
		"""
		if Mouse.current[Mouse.buttons[button]] and not Mouse.previous[Mouse.buttons[button]]:
			return True
		return False

	@classmethod
	def buttonReleased(cls, button):
		"""
		Returns whether a button was released in the last update
		"""
		if not Mouse.current[Mouse.buttons[button]] and Mouse.previous[Mouse.buttons[button]]:
			return True
		return False
