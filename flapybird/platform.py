import pygame

class Platform:

	def __init__(self, Arena_Game):
		self.screen = Arena_Game.screen
		self.screen_rect = self.screen.get_rect()

		self.settings = Arena_Game.game_settings
		self.image = self.settings.platform_image
		self.image_rect = self.image.get_rect()
		self.scaleWidth()
		self.image_rect.midbottom = self.screen_rect.midbottom

		#tambahan posisi khusus x
		self.x = self.image_rect.x

	def scaleWidth(self):
		height = self.image_rect.height
		width2x = self.image_rect.width * 2
		self.image = pygame.transform.scale(self.image, (width2x, height))

	def move(self):
		if self.image_rect.centerx <= self.screen_rect.left:
			self.x = 0
		self.x -= self.settings.platform_speed
		self.image_rect.x = self.x

	def show_platform(self):
		self.screen.blit(self.image, self.image_rect)