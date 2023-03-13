'''
Created on 1 May 2020

@author: joellaitila
'''

from PyQt5.QtWidgets import (
    QGraphicsRectItem,
    QGraphicsScene
)

class Platform(QGraphicsScene):
    def __init__(self, scene, color, x, y, w, h):  
        self.x = x
        self.y = y
        self.w = w     
        self.h = h
        self.scene = scene
        self.platform = QGraphicsRectItem()
        self.platform.setRect(self.x, self.y, self.w, self.h)
        self.platform.setBrush(color)
        self.scene.addItem(self.platform)
        #adds the platform in the scene
    
    def get_x(self):
        return self.x
        #returns the x-coordinate of the platform    
    
    def get_y(self):
        return self.y
        #returns the y-coordinate of the platform
        
    def get_w(self):
        return self.w
        #returns the width of the platform
    
    def get_h(self):
        return self.h
        #returns the height of the platform
    
    def set_w(self, value):
        self.w = value
    
    def move_x(self, new_value):
        self.x += new_value
        self.platform.setRect(self.get_x(), self.get_y(), self.get_w(), self.get_h())
        #moves the platforms when moving the player

                        