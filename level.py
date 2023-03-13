'''
Created on 1 May 2020

@author: joellaitila
'''
from background import Background
from platform import Platform
from settings import *

class Level():
    def __init__(self, scene, level, size):
        self.level = level
        self.size = size
        self.background_list = []
        self.x = 0
        self.y = 0
        self.scene = scene
        self.last_scene = None
        self.goal = None
        self.platform_list = []
        
    def create_background(self, photo):
        for i in range(self.size):
            b = Background(photo, parent = None)
            self.background_list.append(b)
            b.setPos(self.x, self.y)
            self.scene.addItem(b)
            self.x += WIDTH
        self.last_scene = self.background_list[-1]   
        
    def create_platforms(self, platforms, color):
        for platform in platforms:
            if platform == platforms[-1]:
                p = Platform(self.scene, GREEN, *platform)
                self.goal = p
            else:
                p = Platform(self.scene, color, *platform)
            self.platform_list.append(p)

