#This is game.py - the main game logic for Bomberman
import pygame
from character import Character
from blocks import Hard_block
import gamesetting as gs

class Game:
  def __init__(self, main, assets):
    # LINK WITH MAIN CLASS AND ASSETS
    self.MAIN = main
    self.ASSETS = assets

    # Player Character 
    self.PLAYER = Character(self,self.ASSETS.player_char)

    # Groups
    self.hard_blocks = pygame.sprite.Group()

    # Level Information
    self.level = 1
    self.level_matrix = self.generate_level_matrix(gs.ROWS,gs.COLS)

  def input(self):
    self.PLAYER.input()

  def update(self):
    self.hard_blocks.update()
    self.PLAYER.update()


  def draw(self,window):
    self.hard_blocks.draw(window)
    self.PLAYER.draw(window)

  def generate_level_matrix(self,rows,cols):
    """Generate the basic level matrix"""
    matrix = []
    for row in range(rows):
      line = []
      for col in range(cols):
        line.append("_")
      matrix.append(line)
    self.insert_hard_block_into_matrix(matrix)  
    for row in matrix:
      print(row)
    return matrix
      

  def insert_hard_block_into_matrix(self,matrix):
    """Insert all of the Hard Barrier Block into the level of matrix"""
    LAST_ROW = len(matrix) - 1

    if not matrix or not matrix[0]:
        return
    LAST_COL = len(matrix[0]) - 1       
    
    for row_num, row in enumerate(matrix):
       for col_num, col in enumerate(row):
         
         if row_num == 0 or row_num == LAST_ROW or \
             col_num == 0 or col_num == LAST_COL or \
               (row_num % 2 == 0 and col_num % 2 == 0):
           matrix[row_num][col_num] = Hard_block(self,
                                              self.ASSETS.hard_block["hard_block"],
                                              self.hard_blocks,
                                              row_num, col_num)
    return
    # for row_num, row in enumerate(matrix):
    #   for col_num, col in enumerate(row):
    #     if row_num == 0 or row_num == len(matrix)-1 or \
    #         col_num == 0 or col_num == len(row)-1 or \
    #           (row_num % 2 == 0 and col_num % 2 == 0):
    #      matrix[row_num][col_num] = Hard_block(self, # Pass the Game instance
    #                                   self.ASSETS.hard_block["hard_block"], 
    #                                   self.hard_blocks,
    #                                   row_num, col_num)
    # return           
