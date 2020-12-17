import pygame
from pygame.sprite import Sprite


class Head:

	def __init__(self):
		self.width = 60
		self.height = 25
		self.head_rect = pygame.Rect(0, 0, self.width, self.height)


class Pipe(Sprite):

	def __init__(self, Arena_Game):
		super().__init__()

		self.screen = Arena_Game.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = Arena_Game.game_settings

		self.pipe_image = pygame.Rect(0, 0, self.settings.pipe_width, self.settings.pipe_height)
		self.pipe_image.topright = self.screen_rect.topright

		#self.pipe_image.x -= 50
		self.x = self.pipe_image.x

		#set posisi awal pipe
		self.resetposition()
		###HEAD
		self.head = Head()
		#self.head.head_rect.midbottom = self.pipe_image.midbottom


	def resetposition(self):
		self.x = self.screen_rect.right + 100
		self.pipe_image.x = self.x

	def move(self):
		self.x -= self.settings.pipe_speed
		self.pipe_image.x = self.x
		self.head.head_rect.centerx = self.pipe_image.centerx


	def show_pipe(self):
		pygame.draw.rect(self.screen, self.settings.pipe_color, self.pipe_image)
		pygame.draw.rect(self.screen, self.settings.pipe_color, self.head.head_rect)
