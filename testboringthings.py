import core


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
