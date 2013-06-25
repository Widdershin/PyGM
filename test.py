import time
import core


class Character(core.PyGMObj):
	"""Character yo"""
	def __init__(self, x, y, sprite=None):
		super(Character, self).__init__(x, y, sprite)

	def update(self):
		super(Character, self).update()
		self.x += 1
		self.y += 1
		print 'updating'


def main():
	game = core.PyGM(width=800, height=600, fps=60)

	player = Character(x=50, y=50, sprite='Sprites\\Test.png')
	game.objects.append(player)

	while True:
		time.sleep(1 / 60 * 1000)
		game.update()
		game.draw()

if __name__ == '__main__':
	main()
