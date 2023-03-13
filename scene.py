'''
Created on 1 May 2020

@author: joellaitila
'''

from PyQt5.QtCore import (
    Qt,
    QBasicTimer
)
from PyQt5.QtGui import (
    QPixmap
)
from PyQt5.QtWidgets import (
    QGraphicsPixmapItem,
    QGraphicsScene,
)

from level import Level
from player import Player
from settings import *


class Scene(QGraphicsScene):
    def __init__(self, parent = None):
        QGraphicsScene.__init__(self, parent)
        self.initScene()
        
    def initScene(self): 
        self.keys_pressed = set()
        self.timer = QBasicTimer()    
        self.first_game = True 
        self.start_screen = True
        self.level_1_finished = False
        self.level_2_finished = False 
        self.level_3_finished = False
        self.completed = False
        self.set_up_game()
        
    def keyPressEvent(self, event):
        self.keys_pressed.add(event.key())

    def keyReleaseEvent(self, event):
        self.keys_pressed.remove(event.key())

    def timerEvent(self, event):
        self.game_update()
        self.update()

    def set_up_game(self):
        self.running = False
        self.timer.start(FPS, self)
        self.clear()
        if self.start_screen:
            self.start = Level(self, 0, 1)
            self.start.create_background("lvl1_background.jpg")
            self.set_start_photo("startscreen.png", 100, 50)
            #creates start screen when the application is launched
            
        elif not self.level_1_finished:
            self.current_level_finished = False 
            self.level_1 = Level(self, 1, 2)
            self.level_1.create_background("lvl1_background.jpg")
            self.level_1.create_platforms(LVL1_PLATFORMS, RED)
            self.background_list = self.level_1.background_list
            self.platform_list = self.level_1.platform_list
            self.current_level = self.level_1
            self.goal = self.level_1.goal
            if self.first_game:
                self.set_start_photo("lvl1.png")
            else:
                self.set_start_photo("gameover.png")
            #creates level 1 if it's not finished
      
        elif not self.level_2_finished:
            self.current_level_finished = False 
            self.level_2 = Level(self, 2, 3)
            self.level_2.create_background("lvl2_background.png")
            self.level_2.create_platforms(LVL2_PLATFORMS, BLUE)
            self.background_list = self.level_2.background_list
            self.platform_list = self.level_2.platform_list
            self.current_level = self.level_2
            self.goal = self.level_2.goal
            self.set_start_photo("lvl2.png")
            #creates level 2 after level 1 is finished
            
        elif not self.level_3_finished:
            self.current_level_finished = False 
            self.level_3 = Level(self, 3, 4)
            self.level_3.create_background("lvl3_background.jpg")
            self.level_3.create_platforms(LVL3_PLATFORMS, BLACK)
            self.background_list = self.level_3.background_list
            self.platform_list = self.level_3.platform_list
            self.current_level = self.level_3
            self.goal = self.level_3.goal
            self.set_start_photo("lvl3.png")
            #creates level 3 after level 2 is finished
            
        else:
            self.game_completed = Level(self, 4, 1)
            self.game_completed.create_background("lvl3_background.jpg")
            self.set_start_photo("game_completed.png", 100,50)
            self.compeleted = True
            self.first_game = True 
            self.level_1_finished = False
            self.level_2_finished = False
            self.level_3_finished = False
            #game is completed so it can start over again
    
    def set_start_photo(self, photo, x = 200, y = 100):
        self.start_photo = QGraphicsPixmapItem()
        self.start_photo.setPixmap(QPixmap(photo))
        self.start_photo.setPos(x, y)
        self.addItem(self.start_photo)
        #puts a start photo on the screen
          
    def game_update(self):
        if self.start_screen and Qt.Key_Space in self.keys_pressed:
            self.start_screen = False
            self.set_up_game()
            #creates a start screen if the game has just started
            
        elif self.completed and Qt.Key_Space in self.keys_pressed:
            self.completed = False
            self.current_level_finished = False
            self.set_up_game()    
            #restarts the game after the player has finished it
            
        elif not self.running:
            if Qt.Key_Space in self.keys_pressed:
                self.removeItem(self.start_photo)
                self.player = Player(self)
                self.player.setPos(100,100)
                self.addItem(self.player)
                self.running = True
                BACKTRACK.play()
            #after game over/passing the level, \
            #this function starts the level when player presses space
            
        elif self.running:
            self.player.update(self.keys_pressed)
            #updates player movement etc events happened when playing    
    