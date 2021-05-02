# from PyQt5 import QtCore, QtGui, QtWidgets

from pyqtgraph.Qt import QtCore, QtGui, QtWidgets

import cv2
import serial
import sys
import time

class CameraThread(QtCore.QThread):
    ImageUpdate = QtCore.pyqtSignal(QtGui.QImage)
    def __init__(self,CameraLabel = 0 ):
        super().__init__()
        self.CameraLabel = CameraLabel
    def run(self):
        self.threadActive = True
        if self.CameraLabel != 0:
            try:
                Capture = cv2.VideoCapture(str(self.CameraLabel))
            except:
                Capture = cv2.VideoCapture(0)
        else:
            Capture = cv2.VideoCapture(0)
        
        while self.threadActive:
            ret, frame = Capture.read()
            if ret:
                Image = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
                FlippedImage = cv2.flip(Image,1)
                ConvertToQtFormat =QtGui.QImage(FlippedImage.data, FlippedImage.shape[1], FlippedImage.shape[0], QtGui.QImage.Format_RGB888)
                Pic = ConvertToQtFormat.scaled(640, 480,QtCore.Qt.KeepAspectRatio)
                self.ImageUpdate.emit(Pic)

    def stop(self):
        self.ThreadActive = False
        self.quit()