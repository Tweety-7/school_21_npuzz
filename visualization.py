import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import numpy as np
from Visualizator import Visualizator

COLOR_BLACK = (0, 0, 0)
COLOR_GREY = (0xA, 0xA, 0xA)
INNER_GRID_WIDTH = 1

def run_visualization(size, h, w, grid, tile_size, grid_full):
	pygame.init()
	os.environ['SDL_VIDEO_CENTERED'] = '1'
	pygame.display.set_caption("NPuzzle")
	screen = pygame.display.set_mode((h, w))
	fpsclock = pygame.time.Clock()
	program = Visualizator((size, size), tile_size, INNER_GRID_WIDTH, grid, grid_full)
	while True:
		dt = fpsclock.tick() / 1000
		screen.fill(COLOR_GREY)
		program.draw(screen)
		pygame.display.flip()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()
			program.events(event)
		program.update(dt)

def visualizate(grid, steps, n):
	if n > 16:
		print("Max puzzle size for visualization is 16")
		return
	if steps == None:
		print("Visualizer is useless if puzzle is already solved.")
		return
	if n > 4:
		tile_size = int(800 / n)
		h, w = tile_size * n + n * 5, tile_size * n + n * 5
	else:
		h, w = 200 * n + n * 5, 200 * n + n * 5
		tile_size = 200
	steps.insert(0, grid)
	run_visualization(n, h, w, np.concatenate(grid), tile_size, steps)