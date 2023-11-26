'''
Created on 21 Apr 2020 

@author: joellaitila
'''
import sys
from PyQt6.QtWidgets import (
    QApplication,
    QGraphicsView,
    QMainWindow,
    QWidget,
    QHBoxLayout

)
from PyQt6.QtCore import (
    Qt, QRect
)
from scene import Scene
from settings import *
      
# Executing this file starts the game
# The MainWindow class creates the GUI

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setCentralWidget(QWidget())
        self.statusbar = self.statusBar()
        self.horizontal = QHBoxLayout()
        self.centralWidget().setLayout(self.horizontal)
        self.init_window()  
        self.center()
      
    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    
    def init_window(self):
        self.resize(WIDTH+1, HEIGHT+1)
        self.setWindowTitle(TITLE)
        self.show()
        self.scene = Scene()
        self.view = QGraphicsView(self.scene, self) 
        self.view.verticalScrollBar().setEnabled(False)
        self.view.horizontalScrollBar().setEnabled(False)
        self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.view.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.view.setFixedSize(WIDTH, HEIGHT)
        self.view.centerOn(0,0)
        self.view.show()
        self.horizontal.addWidget(self.view)
        #setting up the window settings

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()

    sys.exit(app.exec())
    
