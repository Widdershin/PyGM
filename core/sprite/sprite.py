import pygame
import pygame.sprite


class Sprite(pygame.sprite.Sprite):
	"""Sprite object yo"""
	def __init__(self, spriteFile, surface):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(spriteFile).convert()
		print self.image
		self.spriteFile = spriteFile
		self.group = pygame.sprite.Group()
		self.add(self.group)
		self.screen = pygame.display.get_surface()
		self.rect = self.image.get_rect()

	def draw(self, position):
		#self.group.draw()
		self.screen.blit(self.image, position.tuple())
