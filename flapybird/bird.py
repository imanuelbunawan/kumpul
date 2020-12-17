import pygame


class Bird:

	def __init__(self, Arena_Game):
		#Init Screen For Bird
		self.screen = Arena_Game.screen
		self.screen_rect = Arena_Game.screen.get_rect()

		#Init Bird Image
		self.game_settings = Arena_Game.game_settings
		self.image = self.game_settings.bird_image
		self.image_rect = self.image.get_rect()

		#Init Bird Position
		self.image_rect.midleft = self.screen_rect.midleft
		self.image_rect.x += 50

	def show_bird(self):
		#Show Bird using Blit from Pygame
		self.screen.blit(self.image, self.image_rect)