'''
Created on 21 Apr 2020 

@author: joellaitila
'''
import sys
from PyQt5.QtWidgets import (
    QApplication,
    QGraphicsView,
    QDesktopWidget,
    QMainWindow,
    QWidget,
    QHBoxLayout

)
from PyQt5.QtCore import (
    Qt
)
from scene import Scene
from settings import *
      
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
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())//2, (screen.height()-size.height())//2)
        #centers the window on the screen
    
    def init_window(self):
        self.resize(WIDTH+1, HEIGHT+1)
        self.setWindowTitle(TITLE)
        self.show()
        self.scene = Scene()
        self.view = QGraphicsView(self.scene, self) 
        self.view.verticalScrollBar().setEnabled(False)
        self.view.horizontalScrollBar().setEnabled(False)
        self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.setFixedSize(WIDTH, HEIGHT)
        self.view.centerOn(0,0)
        self.view.show()
        self.horizontal.addWidget(self.view)
        #setting up the window settings

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()

    sys.exit(app.exec_())
    
