'''
Created on 1 May 2020

@author: joellaitila
'''
from PyQt5.QtWidgets import (
    QGraphicsPixmapItem
)
from PyQt5.QtGui import (
    QPixmap
)

class Background(QGraphicsPixmapItem):
    def __init__(self, photo, parent = None):
        QGraphicsPixmapItem.__init__(self,parent)
        self.setPixmap(QPixmap(photo))

    def move_x(self, new_value):
        self.setX(self.x() + new_value)
        self.setPos(self.x(), self.y()) 
        #moves the platforms when moving the player
    
    def get_x(self):
        return self.x()
    
        