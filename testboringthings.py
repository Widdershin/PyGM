import core
import core.maths


class Player(core.PyGMObj):
	def __init__(self, x, y, sprite=None):
		super(Player, self).__init__(x, y, sprite)


class Nick(Player):
	"""docstring for Nick"""
	def __init__(self, x, y, sprite=None):
		super(Nick, self).__init__(x, y, sprite)
		self.x = x
		self.y = y
		self.sprite = sprite


a = Player(5, 5)
b = Player(10, 5)
c = Nick(1, 3)

print 'Nick: ' + str(Nick.instances())
print 'Player: ' + str(Player.instances())

a1 = maths.Vector2(5, 5)
a2 = maths.Vector2(10, 25)

print a1
print a2

print a1 + a2
print a1 - a2
print a1 * 5
print a1 * a2
print a1 / 3
print a1 / a2
