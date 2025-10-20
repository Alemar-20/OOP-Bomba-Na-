#This is blocks.py - defines block classes for the Bomberman game
import pygame
import gamesetting as gs

class Blocks(pygame.sprite.Sprite):
  def __init__(self,game,images,group,row_number,col_number):
    super().__init__(group)
    self.GAME = game

    # BLOCK POSITION
    self.row = row_number
    self.col = col_number
    #self.x = col_number * gs.SIZE
    #self.y = row_number * gs.SIZE

    # Cell size
    self.size = gs.SIZE

    # Coordinates of block
    self.x = self.col * self.size
    self.y = self.row * self.size

    # Atrributes
    self.passable = False


    # BLOCK DISPLAY
    self.image_list = images
    self.image_index = 0
    self.image = self.image_list[self.image_index]
    self.rect = self.image.get_rect(topleft=(self.x, self.y))

  def update(self):
   pass

  def draw(self,window):
    window.blit(self.image, self.rect)

  def __repr__(self):
    return "'#'"
  

class Hard_block(Blocks):
  def __init__ (self, game, images, group, row_number, col_number):
    super().__init__(game, images, group, row_number, col_number)
