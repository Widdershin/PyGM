import time
import core
from core.input import Keys, Mouse
import core.maths as maths

class Character(core.PyGMObj):
	"""Character yo"""
	def __init__(self, position, sprite=None):
		super(Character, self).__init__(position, sprite)

	def update(self):
		super(Character, self).update()
		if Keys.keyDown('w'):
			self.position.y -= 1
		if Keys.keyDown('s'):
			self.position.y += 1
		if Keys.keyDown('d'):
			self.position.x += 1
		if Keys.keyDown('a'):
			self.position.x -= 1

		self.position = Mouse.position

		print Mouse.position


def main():
	game = core.PyGM(dimensions=maths.Vector2(800, 600), fps=60)
	Character(maths.Vector2(50, 50), sprite='Sprites\\Test.png')

	while True:
		time.sleep(1 / 60 * 1000)
		game.update()
		game.draw()

if __name__ == '__main__':
	main()
