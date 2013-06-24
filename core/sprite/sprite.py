import pygame
import pygame.sprite


class Sprite(pygame.sprite.Sprite):
	"""Sprite object yo"""
	def __init__(self, spriteFile, surface):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(spriteFile)
		print self.image
		self.spriteFile = spriteFile
		self.group = pygame.sprite.Group()
		self.add(self.group)
		self.screen = pygame.display.get_surface()

	def draw(self):
		#self.group.draw()
		self.screen.blit(self.image, (0, 0))
		print 'drawing'
