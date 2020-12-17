import pygame

class Settings:
	def __init__(self):

		#Arena Settings
		self.screen_width = 360
		self.screen_height = 640
		self.title = "Flappy Bird"
		self.background = pygame.image.load("img/bg.PNG")


		#Bird Settings
		self.bird_image = pygame.image.load("img/bird.PNG")

		#Platform Settings
		self.platform_image = pygame.image.load("img/land.PNG")
		self.platform_speed = 1
		#self.platform_image = pygame.transform.scale2x(self.platform_image)

		#Pipe Settings
		self.pipe_width = 50
		self.pipe_height = 200
		self.pipe_color = [60, 60, 60]
		self.pipe_speed = 1
