'''
Created on 21 Apr 2020

@author: joellaitila
'''
from PyQt6.QtGui import (
    QColor
)
from PyQt6.QtCore import (
    QDir,
    QUrl
)
from PyQt6.QtMultimedia import (
    QMediaPlayer,
)


#GAME SETTINGS

TITLE = "Tasohyppelypeli"
WIDTH = 1000
HEIGHT = 500
FPS = 16

#PLAYER SETTINGS

P_ACC = 0.5
P_FRICTION = -0.08
P_GRAVITY = 0.3

#COLORS

WHITE = QColor(255, 255, 255)
BLACK = QColor(0, 0, 0)
RED = QColor(255, 0, 0)
GREEN = QColor(0, 255, 0)
BLUE = QColor(0, 0, 255)

#SOUNDSETTINGS
"""
    #JUMP

jump_path = QDir.current().absoluteFilePath('audio_jump_1.mp3') 
jump_content = QMediaContent(QUrl.fromLocalFile(jump_path))
JUMP = QMediaPlayer()
JUMP.setMedia(jump_content)
JUMP.setPlaybackRate(2)
 
    #DEATH
    
death_path = QDir.current().absoluteFilePath('audio_death_1.mp3') 
death_content = QUrl.fromLocalFile(death_path)
DEATH = QMediaPlayer()
DEATH.setMedia(death_content)
    
    #VICTORY

victory_path = QDir.current().absoluteFilePath('audio_victory_1.mp3') 
victory_content = QUrl.fromLocalFile(victory_path)
VICTORY = QMediaPlayer()
VICTORY.setMedia(victory_content)
VICTORY.setVolume(40)
    
    #BACKTRACK

backtrack_path = QDir.current().absoluteFilePath('audio_backtrack.mp3') 
backtrack_content = QUrl.fromLocalFile(backtrack_path)
playlist = QMediaPlaylist()
playlist.addMedia(backtrack_content)
playlist.setPlaybackMode(QMediaPlaylist.Loop)
BACKTRACK = QMediaPlayer()
BACKTRACK.setPlaylist(playlist)
BACKTRACK.setVolume(40)

"""

#LEVEL SETTINGS - PLATFORMS (X, Y, WIDTH, HEIGHT)

LVL1_PLATFORMS = [(0, HEIGHT - 40, 300, 40),
             (200, HEIGHT - 220, 100, 10),
             (400, HEIGHT - 150, 200, 10),
             (700, HEIGHT - 200, 150, 10),
             (950, HEIGHT - 40, 300, 40),
             (1350, HEIGHT - 170, 200, 10),
             (1700, HEIGHT - 100, 150, 10),
             (1900, HEIGHT - 40, 200, 40)
             ]

LVL2_PLATFORMS = [(0, HEIGHT - 200, 200, 40),
             (400, HEIGHT - 150, 150, 10),
             (700, HEIGHT - 200, 80, 10),
             (950, HEIGHT - 40, 300, 40),
             (1400, HEIGHT - 160, 200, 10),
             (1700, HEIGHT - 270, 150, 10),
             (2100, HEIGHT - 370, 130, 10),
             (2100, HEIGHT - 100, 100, 10),
             (2400, HEIGHT - 320, 160, 10),
             (2700, HEIGHT - 170, 80, 10),
             (2900, HEIGHT - 40, 100, 40)
             ]

LVL3_PLATFORMS = [(0, HEIGHT - 40, 200, 40),
             (400, HEIGHT - 150, 100, 10),
             (700, HEIGHT - 200, 50, 10),
             (950, HEIGHT - 220, 100, 10),
             (1400, HEIGHT - 160, 100, 10),
             (1700, HEIGHT - 270, 80, 10),
             (2100, HEIGHT - 250, 80, 10),
             (2400, HEIGHT - 320, 100, 10),
             (2700, HEIGHT - 170, 80, 10),
             (2950, HEIGHT - 220, 150, 10),
             (3300, HEIGHT - 250, 80, 10),
             (3550, HEIGHT - 350, 80, 10),
             (3900, HEIGHT - 40, 100, 40)
             ]


