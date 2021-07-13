import pygame
import numpy as np

class Visualizator:
	def __init__(self, grid_size, ts, ms, grid, grid_full):
		self.grid_size, self.ts, self.ms = grid_size, ts, grid_size
		self.tiles_len = grid_size[0] * grid_size[1] - 1
		self.tiles = [(x, y) for y in range(grid_size[1]) for x in range(grid_size[0])]
		self.tiles_v = [x for x in grid]

		self.tilespos = [(x*(ts+ms)+ms,y*(ts+ms)+ms) for y
            in range(grid_size[1])
            for x in range(grid_size[0])]
		self.tilesPOS = {(x,y):(x*(ts+ms)+ms,y*(ts+ms)+ms) for y
            in range(grid_size[1])
            for x in range(grid_size[0])}
		self.prev = None
		self.resolution, self.i, self.reverse, self.next = 1, 1, 0, 0
		self.speed_slide = 450
		self.images = []
		self.grid_full = grid_full
		self.grid_sol = np.concatenate(grid_full[-1])
		w, h = grid_size[0] * (ts + ms) + ms, grid_size[1] * (ts + ms) + ms
		self.rect = pygame.Rect(0, 0, grid_size[0] * (ts + ms) + ms, grid_size[1] * (ts + ms) + ms)
		pic = pygame.transform.smoothscale(pygame.image.load("resources/default.jpg"), self.rect.size)
		for i in grid:
			x, y = self.tilespos[np.where(self.grid_sol == i)[0][0]]
			image = pic.subsurface(x, y, ts, ts)
			self.images += [image]

	def get_blank(self):
		for i in range(len(self.tiles_v)):
			if self.tiles_v[i] == 0:
				return self.tiles[i]

	def set_blank(self, pos):
		for i in range(len(self.tiles_v)):
			if self.tiles_v[i] == 0:
				self.tiles[i] = pos

	opentile = property(get_blank, set_blank)

	def sliding(self):
		for i in range(self.tiles_len):
			x, y = self.tilespos[i]
			xx, yy = self.tilesPOS[self.tiles[i]]
			if x != xx or y != yy:
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
				if state[y][x] == 0:
					return x, y
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
			x, y = self.tilespos[i]
			xx, yy = self.tilesPOS[self.tiles[i]]
			dx, dy = xx - x, yy - y
			x = xx if abs(dx) < s else x + s if dx > 0 else x - s
			y = yy if abs(dy) < s else y + s if dy > 0 else y - s
			self.tilespos[i] = x, y
		pass

	def draw(self, screen):
		for i in range(self.tiles_len + 1):
			x, y = self.tilespos[i]
			screen.blit(self.images[i], (x, y))

	def events(self, event):
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				pygame.quit()
				exit()
			if event.key == pygame.K_MINUS or event.key == pygame.K_KP_MINUS:
				if self.speed_slide > 50:
					self.speed_slide -= 20
			if event.key == pygame.K_PLUS or event.key == pygame.K_KP_PLUS:
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