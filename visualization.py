import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import numpy as np
from Visualizator import Visualizator
from const import *
from images import create_image



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
	if n > 4:
		tile_size = int(800 / n)
		h, w = tile_size * n + n * 5, tile_size * n + n * 5
	else:
		a = 100
		h, w = a * n + n * 5, a * n + n * 5
		tile_size = a
	steps.insert(0, grid)
	run_visualization(n, h, w, np.concatenate(grid), tile_size, steps)


def handle_visualizer(success, b, size_matr, sp_z, min):
	if success and Mode.VIS_MODE and not Mode.BENCHMARK_MODE:
		schema = [int(x) for x in b.split("/")]
		schema = [x.tolist() for x in np.array_split(schema, size_matr)]

		path = get_path2(min, sp_z)
		start_board = path[-1][:]
		fullpath = []
		for p in path:
			p = [int(x) for x in p]
			fullpath.append([x.tolist() for x in np.array_split(p, size_matr)])
		create_image(start_board)
		visualizate(schema, fullpath, size_matr)


def get_path2(min, sp_z):
    sp_path = []
    while min:
        sp_path.append(min.node)
        min = sp_z[min]
    sp_path.reverse()
    return sp_path

def get_path(min, sp_z):
    sp_path = []
    while min:
        sp_path.append(min.node)
        for min_2 in sp_z:
            if (min.par == min_2):
                min =min_2
                break
            if min_2 == sp_z[-1]:
                min = 0
    sp_path.reverse()
    return sp_path