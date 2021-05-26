import sys, os, time
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import numpy as np

class NPuzzle:
	def __init__(self, gs, ts, ms, grid, grid_full):
		self.gs, self.ts, self.ms = gs, ts, gs
		self.tiles_len = gs[0] * gs[1] - 1
		self.tiles = [(x,y) for y in range(gs[1]) for x in range(gs[0])]
		self.tiles_v = [x for x in grid]
		self.tilespos = [(x*(ts+ms)+ms,y*(ts+ms)+ms) for y in range(gs[1]) for x in range(gs[0])]
		self.tilesPOS = {(x,y):(x*(ts+ms)+ms,y*(ts+ms)+ms) for y in range(gs[1]) for x in range(gs[0])}
		self.prev = None
		self.resolution, self.i, self.reverse, self.next = 1, 1, 0, 0
		self.speed_slide = 450
		
		self.images = []
		self.grid_full = grid_full
		self.grid_sol = np.concatenate(grid_full[-1])
		w, h = gs[0] * (ts + ms) + ms, gs[1] * (ts + ms) + ms
		self.rect = pygame.Rect(0, 0, gs[0] * (ts + ms) + ms, gs[1] * (ts + ms) + ms)
		pic = pygame.transform.smoothscale(pygame.image.load("resources/default.jpg"), self.rect.size)
		for i in grid:
			x, y = self.tilespos[np.where(self.grid_sol == i)[0][0]]
			image = pic.subsurface(x, y, ts, ts)
			self.images += [image]

	def getBlank(self):
		for i in range(len(self.tiles_v)):
			if self.tiles_v[i] == 0:
				return self.tiles[i]

	def setBlank(self, pos):
		for i in range(len(self.tiles_v)):
			if self.tiles_v[i] == 0:
				self.tiles[i] = pos

	opentile = property(getBlank, setBlank)

	def sliding(self) :
		for i in range(self.tiles_len):
			x, y = self.tilespos[i]
			X, Y = self.tilesPOS[self.tiles[i]]
			if x != X or y != Y:
				return True
		return False

	def switch(self, tile):
		if self.sliding() == True:
			return
		self.tiles[self.tiles.index(tile)], self.opentile, self.prev = self.opentile, tile, self.opentile

	def	get_empty(self, state):
		x = 0
		while x != len(state[0]):
			y = 0
			while y != len(state[0]):
				if (state[y][x] == 0):
					return (x, y)
				y += 1
			x += 1

	def update(self, dt):
		if len(self.grid_full) == self.i:
			self.resolution = 0
			self.next = 0
		if self.i < 2:
			self.reverse = 0
		if (self.resolution == 1 or self.next == 1) and self.sliding() == False:
			self.switch(self.get_empty(self.grid_full[self.i]))
			self.i += 1
			self.next = 0
		if self.reverse == 1 and self.sliding() == False:
			self.i -= 1
			self.switch(self.get_empty(self.grid_full[self.i - 1]))
			self.reverse = 0
		s = self.speed_slide * dt
		for i in range(self.tiles_len + 1):
			x,y = self.tilespos[i]
			X,Y = self.tilesPOS[self.tiles[i]]
			dx, dy = X - x, Y- y
			x = X if abs(dx) < s else x + s if dx > 0 else x - s
			y = Y if abs(dy) < s else y + s if dy > 0 else y - s
			self.tilespos[i] = x,y
		pass

	def draw(self, screen):
		for i in range(self.tiles_len + 1):
			x,y = self.tilespos[i]
			screen.blit(self.images[i], (x, y))

	def events(self, event):
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				pygame.quit()
				exit()
			if event.key == pygame.K_KP_MINUS:
				if self.speed_slide > 50:
					self.speed_slide -= 20
			if event.key == pygame.K_KP_PLUS:
				if self.speed_slide < 600:
					self.speed_slide += 20
			if event.key == pygame.K_r and self.resolution == 0:
				self.resolution = 1
			elif event.key == pygame.K_r and self.resolution == 1:
				self.resolution = 0
				self.reverse = 0
			if event.key == pygame.K_RIGHT and self.resolution == 0:
				self.reverse = 1
			if event.key == pygame.K_LEFT and self.resolution == 0:
				self.next = 1

def main(size, h, w, grid, size_ts, grid_full):
	pygame.init()
	os.environ['SDL_VIDEO_CENTERED'] = '1'
	pygame.display.set_caption("NPuzzle")
	screen = pygame.display.set_mode((h, w))
	fpsclock = pygame.time.Clock()
	program = NPuzzle((size, size), size_ts, 5, grid, grid_full)
	while True:
		dt = fpsclock.tick() / 1000
		screen.fill((0, 0, 0))
		program.draw(screen)
		pygame.display.flip()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()
			program.events(event)
		program.update(dt)

def visu(grid, steps, n):
	if n > 20:
		print("Max puzzle size is 20x20, otherwise it does not fit the screen.")
		return
	if steps == None:
		print("Visualizer is useless if puzzle is already solved.")
		return
	if n > 4:
		size_ts = int(800 / n)
		h, w = size_ts * n + n * 5, size_ts * n + n * 5
	else:
		h, w = 200 * n + n * 5, 200 * n + n * 5
		size_ts = 200
	steps.insert(0, grid)
	main(n, h, w, np.concatenate(grid), size_ts, steps)