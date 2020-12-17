import pygame
from random import randint


from settings import Settings
from bird import Bird
from pipe import Pipe
from platform import Platform

class Arena_Game:

	################################
	#ARENA / SCREEN
	################################
	def __init__(self):
		pygame.init()
		self.game_settings = Settings()

		self.screen = pygame.display.set_mode([self.game_settings.screen_width, self.game_settings.screen_height])
		self.title = pygame.display.set_caption(self.game_settings.title)
		self.running = True

		############
		#OBJ IN GAME
		############
		#SINGLE OBJ
		self.game_bird = Bird(self)
		self.game_platform = Platform(self)

		#GROUP OBJ
		self.game_pipes = pygame.sprite.Group()
		self.create_pipes()

	def update_bg_screen(self):
		self.screen.blit(self.game_settings.background, [0,0])

	###############################
	#BIRD
	###############################
	def update_bird(self):
		self.game_bird.show_bird()


	###############################
	#PLATFORM
	###############################
	def update_platform(self):
		self.game_platform.move()
		self.game_platform.show_platform()


	###############################
	#PIPE
	###############################
	def update_pipes(self):
		for pipe in self.game_pipes.sprites():
			pipe.move()
			pipe.show_pipe()

	def create_pipes(self):
		screen_rect = self.screen.get_rect()
		screen_height = screen_rect.height

		pipe_top_height = randint(100, 454)
		pipe_bottom_height = 640 - pipe_top_height - 100

		pipe_top = Pipe(self)
		pipe_bottom = Pipe(self)

		pipe_top.pipe_image.height = pipe_top_height #set ulang tinggi pipe_top
		pipe_bottom.pipe_image.height = pipe_bottom_height #set ulang tinggi pipe_bottom

		pipe_bottom.pipe_image.midtop = pipe_top.pipe_image.midbottom #set ulang posisi pipe_bottom
		pipe_bottom.pipe_image.y += 100 #memberikan jarak antara pipe_top dan pipe_bottom
		pipe_top.head.head_rect.midbottom = pipe_top.pipe_image.midbottom #set posisi head pipe_top
		pipe_bottom.head.head_rect.midtop = pipe_bottom.pipe_image.midtop #set posisi head pipe_bottom

		self.game_pipes.add(pipe_top)
		self.game_pipes.add(pipe_bottom)


	################################
	#RUN GAME
	################################
	def rg_check_events(self):
		events = pygame.event.get()
		#print(events)
		for event in events:
			if event.type == pygame.QUIT:
				self.running = False

	def rg_update_screen(self):
		self.update_bg_screen() #Update BG
		self.update_bird() # Update Bird Postision
		self.update_pipes() #Update Pipes
		self.update_platform()
		pygame.display.flip() #Update Frame Every Second


	def run_game(self):
		while self.running:
			self.rg_check_events()
			self.rg_update_screen()

flappy_bird_game = Arena_Game()
flappy_bird_game.run_game()