import time
import core
from core.input import Keys, Mouse


class Character(core.PyGMObj):
	"""Character yo"""
	def __init__(self, x, y, sprite=None):
		super(Character, self).__init__(x, y, sprite)

	def update(self):
		super(Character, self).update()
		if Keys.keyDown('w'):
			self.y -= 1
		if Keys.keyDown('s'):
			self.y += 1
		if Keys.keyDown('d'):
			self.x += 1
		if Keys.keyDown('a'):
			self.x -= 1

		self.x = Mouse.position[0]
		self.y = Mouse.position[1]

		print Mouse.position


def main():
	game = core.PyGM(width=800, height=600, fps=60)
	Character(x=50, y=50, sprite='Sprites\\Test.png')

	while True:
		time.sleep(1 / 60 * 1000)
		game.update()
		game.draw()

if __name__ == '__main__':
	main()
