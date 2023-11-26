'''
Created on 1 May 2020

@author: joellaitila
'''

from PyQt6.QtCore import (
    Qt
)
from PyQt6.QtGui import (
    QPixmap,
    QVector2D
)
from PyQt6.QtWidgets import (
    QGraphicsPixmapItem
)
from settings import *


class Player(QGraphicsPixmapItem):
    def __init__(self, game, parent = None):
        QGraphicsPixmapItem.__init__(self,parent)
        self.setPixmap(QPixmap("0_pingu.png"))
        self.game = game #references the game so we can use the functions in it     
        self.position = QVector2D(100, 100)
        self.velocity = QVector2D(0, 0)
        self.acceleration = QVector2D(0, 0)
        #using acceleration and velocity for a smooth player movement

    def update(self, keys_pressed):
        #setting up player movement by the pressed keys
        #movement itself happens later 
        self.acceleration = QVector2D(0, P_GRAVITY)
        if Qt.Key.Key_Left in keys_pressed:
            self.acceleration.setX(self.acceleration.x() - P_ACC)
        if Qt.Key.Key_Right in keys_pressed:
            self.acceleration.setX(self.acceleration.x() + P_ACC)
        if Qt.Key.Key_Up in keys_pressed:
            self.jump()
            
        #applying friction
        self.acceleration.setX(self.acceleration.x() + self.velocity.x() * P_FRICTION)   
        self.velocity += self.acceleration
        self.position += self.velocity + 0.5 * self.acceleration
        
        #closing the screen left and right borders
        if self.position.x()+self.get_w() >= WIDTH:
            self.position.setX(WIDTH-self.get_w())
        elif self.position.x() <= 0:
            self.position.setX(0)
        
        # checking collision 
        if self.velocity.y() > 0: 
            self.collision, index = self.collisionCheck(self, self.game.platform_list)
            if self.collision == True:
                hitting_plat = self.game.platform_list[index]
                if self.game.goal == hitting_plat:
                    self.game.current_level_finished = True
                    #if the player hits the green platform
                    # -> level is finished
    
                elif self.position.x() + (self.get_w()* (1/3)) < (hitting_plat.get_x() + hitting_plat.get_w()) and \
                    self.position.x() + (self.get_w()* (2/3)) > hitting_plat.get_x():
                    self.position.setY(hitting_plat.get_y() - self.get_h())
                    self.velocity.setY(0)           
                    #otherwise puts player on top of the platform that it collides with 
                
             
        self.setPos(self.position.x(), self.position.y()) 
        #moving the player with or without collision    


        #setting scrolling, so that platforms move along the player
        #this doesn't happen if the player can see the "goal" in the screen
        if self.get_x() >= WIDTH / 4 and self.game.current_level.last_scene.get_x() > 0:
            self.position.setX(self.position.x() - self.velocity.x())
            #won't let player move over certain point
            for platform in self.game.platform_list:
                platform.move_x(-1 * self.velocity.x())
                #moves the platforms
            for b in self.game.background_list:
                b.move_x(-1 * self.velocity.x())
                #moves the backgrounds
                
              
        if self.game.current_level_finished:
            BACKTRACK.stop()
            if self.game.current_level == self.game.level_1:
                self.game.level_1_finished = True
            elif self.game.current_level == self.game.level_2:
                self.game.level_2_finished = True
            elif self.game.current_level == self.game.level_3:
                self.game.level_3_finished = True
                VICTORY.play()
            self.game.timer.stop()
            self.game.set_up_game() 
            #set ups a new level if the player finished the current level
        
        elif self.get_y() > HEIGHT:
            self.game.current_level = self.game.level_1
            self.game.level_1_finished = False
            self.game.level_2_finished = False
            self.game.level_3_finished = False
            self.game.first_game = False 
            self.game.timer.stop()
            BACKTRACK.stop()
            DEATH.play()
            self.game.set_up_game() 
            #player dies and starts a new game 
      
    def jump(self):
        self.position.setY(self.position.y()+1)
        self.collision, index = self.collisionCheck(self, self.game.platform_list)
        self.position.setY(self.position.y()-1)
        #first checks if player is on a platform
        #only if it is, then the player can jump (so one can't keep jumping multiple times)
        if self.collision == True:
            self.velocity.setY(-10)
            JUMP.play()                 

    def detectCollision(self,player, platform):
        x1 = player.get_x()
        y1 = player.get_y()
        w1 = player.get_w()
        h1 = player.get_h()
        x2 = platform.get_x()
        y2 = platform.get_y()
        w2 = platform.get_w()
        h2 = platform.get_h()
        if (x1 < x2 + w2) and (x1 + w1 > x2) and \
           (y1 < y2 + h2) and (y1 + h1 > y2):
            return True
        else:
            return False
        #returns true if player collides with the platform
        
    def collisionCheck(self, player, platform_list):
        colliding_platform = []
        for platform in platform_list:
            collision = self.detectCollision(player, platform)
            colliding_platform.append(collision)
        if True in colliding_platform:
            return True, colliding_platform.index(True)
        else:
            return False, None          
        #if one of the platforms collides with the player, returns True and
        #the index of the platform in the list   
      
    def get_x(self): 
        return self.x()
        #returns the x-coordinate of the player
           
    def get_y(self): 
        return self.y()
        #returns the y-coordinate of the player
    
    def get_w(self):
        return self.pixmap().width()
        #returns the width of the player
       
    def get_h(self):
        return self.pixmap().height()
        #returns the height the player
