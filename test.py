import time
import core


def main():
	game = core.PyGM(width=800, height=600, fps=60)

	while True:
		time.sleep(1 / 60 * 1000)
		game.update()
		game.draw()

if __name__ == '__main__':
	main()
