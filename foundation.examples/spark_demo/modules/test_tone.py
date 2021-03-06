# -*- coding: utf-8 -*-
# RPiSpark Tone Testting
# 
# Author: Kunpeng Zhang
# 2018.5.30
#
# See LICENSE for details.

import random
import os.path
from PIL import Image
from time import sleep

from JMRPiFoundations.Skeleton.RPiSparkModule import RPiSparkModule
from JMRPiSpark.Drives.Audio.RPiTone import TONE_MID, TONE_BASS, TONE_A
from JMRPiSpark.Drives.Audio.RPiTone import RPiTonePlayer

###################################
# Font 
#
FONT_NAME = "AHandMadeFont.ttf"
FONT_SIZE = 28

class TestTone(RPiSparkModule):
    myScreen = None
    myTone = None
    
    def drawToneMode(self, y, toneMode):
        self.myScreen.write(toneMode, xy=(0, y), fontName=FONT_NAME, fontSize=FONT_SIZE, screenCenter=True )

    def _sndTone(self):
        if self.myTone == None: return
        tones = [ 20, 46, 69, 105, 160, 244, 371, 565, 859, 1300, 1980 ]
        for t in tones:
            self.myTone.playTone( freq=t, reps=1, delay=0.1, muteDelay=0.05 )
        self.myTone.stopTone()

    def _sndTone3Tigers(self):
        if self.myTone == None: return
        delay_2 = 0.075
        delay1 = 0.15
        delay2 = 0.3
        muteDelay1 = 0.05
        muteDelay2 = 0.1
        myTONE = TONE_MID[TONE_A]
        myTONE2 = TONE_BASS[TONE_A]

        tone3Tigers = [
            {"freq": myTONE[1], "reps": 1, "delay": delay1, "muteDelay": muteDelay1},
            {"freq": myTONE[2], "reps": 1, "delay": delay1, "muteDelay": muteDelay1},
            {"freq": myTONE[3], "reps": 1, "delay": delay1, "muteDelay": muteDelay1},
            {"freq": myTONE[1], "reps": 1, "delay": delay1, "muteDelay": muteDelay1},
            
            {"freq": myTONE[1], "reps": 1, "delay": delay1, "muteDelay": muteDelay1},
            {"freq": myTONE[2], "reps": 1, "delay": delay1, "muteDelay": muteDelay1},
            {"freq": myTONE[3], "reps": 1, "delay": delay1, "muteDelay": muteDelay1},
            {"freq": myTONE[1], "reps": 1, "delay": delay1, "muteDelay": muteDelay1},
            
            {"freq": myTONE[3], "reps": 1, "delay": delay1, "muteDelay": muteDelay1},
            {"freq": myTONE[4], "reps": 1, "delay": delay1, "muteDelay": muteDelay1},
            {"freq": myTONE[5], "reps": 1, "delay": delay2, "muteDelay": muteDelay1},
            
            {"freq": myTONE[3], "reps": 1, "delay": delay1, "muteDelay": muteDelay1},
            {"freq": myTONE[4], "reps": 1, "delay": delay1, "muteDelay": muteDelay1},
            {"freq": myTONE[5], "reps": 1, "delay": delay2, "muteDelay": muteDelay1},
            
            ################################
            
            {"freq": myTONE[5], "reps": 1, "delay": delay_2, "muteDelay": muteDelay1},
            {"freq": myTONE[6], "reps": 1, "delay": delay_2, "muteDelay": muteDelay1},
            {"freq": myTONE[5], "reps": 1, "delay": delay_2, "muteDelay": muteDelay1},
            {"freq": myTONE[4], "reps": 1, "delay": delay_2, "muteDelay": muteDelay1},
            {"freq": myTONE[3], "reps": 1, "delay": delay1, "muteDelay": muteDelay1},
            {"freq": myTONE[1], "reps": 1, "delay": delay1, "muteDelay": muteDelay1},
            
            {"freq": myTONE[5], "reps": 1, "delay": delay_2, "muteDelay": muteDelay1},
            {"freq": myTONE[6], "reps": 1, "delay": delay_2, "muteDelay": muteDelay1},
            {"freq": myTONE[5], "reps": 1, "delay": delay_2, "muteDelay": muteDelay1},
            {"freq": myTONE[4], "reps": 1, "delay": delay_2, "muteDelay": muteDelay1},
            {"freq": myTONE[3], "reps": 1, "delay": delay1, "muteDelay": muteDelay1},
            {"freq": myTONE[1], "reps": 1, "delay": delay1, "muteDelay": muteDelay1},
            
            {"freq": myTONE[1], "reps": 1, "delay": delay1, "muteDelay": muteDelay1},
            {"freq": myTONE2[5], "reps": 1, "delay": delay1, "muteDelay": muteDelay1},
            {"freq": myTONE[1], "reps": 1, "delay": delay2, "muteDelay": muteDelay1},

            {"freq": myTONE[1], "reps": 1, "delay": delay1, "muteDelay": muteDelay1},
            {"freq": myTONE2[5], "reps": 1, "delay": delay1, "muteDelay": muteDelay1},
            {"freq": myTONE[1], "reps": 1, "delay": delay2, "muteDelay": muteDelay1},
        ]

        self.myTone.playToneList(tone3Tigers)
        self.myTone.stopTone()

    def setup(self):
        random.seed()
        self.myScreen = self.RPiSpark.Screen
        if self.RPiSpark.Tone != None:
            self.myTone = self.RPiSpark.Tone
        else:
            self.myTone = RPiTonePlayer( self.RPiSparkConfig.SPEAKER )

    #Test display
    def run(self):
        self.myScreen.clearCanvas()
        self.drawToneMode(10, "Tone")
        self.myScreen.refresh()

        self._sndTone()
        self._sndTone3Tigers()
        
        print("Tone testting done.")
