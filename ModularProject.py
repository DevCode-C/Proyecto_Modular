# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ModularProject.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


# from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph.Qt import QtCore, QtGui, QtWidgets
from pyqtgraph import *
import pyqtgraph.opengl as gl
from SerialConfiguration import *
# from CameraConfiguration import *
# from CameraFunction import *
import serial
import numpy as np
import random
from grapich3D import *


class Ui_ModularProject(object):
    
    def setupUi(self, ModularProject):
        self.LoopCount = 0
        self.countLoop = 0
        ModularProject.setObjectName("ModularProject")
        ModularProject.resize(1080, 720)
        ModularProject.setMinimumSize(QtCore.QSize(1080, 720))
        ModularProject.setMaximumSize(QtCore.QSize(1280, 805))
        ModularProject.setStyleSheet("background-color: rgb(211, 211, 211);")
        self.centralwidget = QtWidgets.QWidget(ModularProject)
        self.centralwidget.setObjectName("centralwidget")
        self.Pestanas = QtWidgets.QTabWidget(self.centralwidget)
        self.Pestanas.setGeometry(QtCore.QRect(10, 80, 1061, 620))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Pestanas.setFont(font)
        self.Pestanas.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Pestanas.setObjectName("Pestanas")
        self.Principal = QtWidgets.QWidget()
        self.Principal.setObjectName("Principal")
        self.CameraBox = QtWidgets.QFrame(self.Principal)
        self.CameraBox.setGeometry(QtCore.QRect(550, 10, 491, 401))
        self.CameraBox.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.CameraBox.setFrameShape(QtWidgets.QFrame.Box)
        self.CameraBox.setFrameShadow(QtWidgets.QFrame.Plain)
        self.CameraBox.setObjectName("CameraBox")
        self.CameraImage = QtWidgets.QLabel(self.CameraBox)
        self.CameraImage.setGeometry(QtCore.QRect(50, 10, 401, 341))
        self.CameraImage.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.CameraImage.setFrameShadow(QtWidgets.QFrame.Plain)
        self.CameraImage.setLineWidth(1)
        self.CameraImage.setText("")
        self.CameraImage.setPixmap(QtGui.QPixmap("UdeGSPACECamera.png"))
        self.CameraImage.setScaledContents(True)
        self.CameraImage.setObjectName("CameraImage")
        self.ConfigurationButton = QtWidgets.QPushButton(self.CameraBox)
        self.ConfigurationButton.setGeometry(QtCore.QRect(380, 360, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.ConfigurationButton.setFont(font)
        self.ConfigurationButton.setStyleSheet("background-color: rgb(207, 207, 207);")
        self.ConfigurationButton.setObjectName("ConfigurationButton")
        self.lineEdit = QtWidgets.QLineEdit(self.CameraBox)
        self.lineEdit.setGeometry(QtCore.QRect(50, 360, 321, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.PowerSignalViewAtMomentDial = QtWidgets.QDial(self.Principal)
        self.PowerSignalViewAtMomentDial.setGeometry(QtCore.QRect(780, 440, 131, 131))
        self.PowerSignalViewAtMomentDial.setStyleSheet("color: rgb(255, 255, 127);\n"
"background-color: rgb(85, 255, 255);\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(255, 255, 255, 255), stop:0.2 rgba(255, 176, 176, 167), stop:0.3 rgba(255, 151, 151, 92), stop:0.4 rgba(255, 125, 125, 51), stop:0.5 rgba(255, 76, 76, 205), stop:0.52 rgba(255, 76, 76, 205), stop:0.6 rgba(255, 180, 180, 84), stop:1 rgba(255, 255, 255, 0));")
        self.PowerSignalViewAtMomentDial.setOrientation(QtCore.Qt.Horizontal)
        self.PowerSignalViewAtMomentDial.setInvertedAppearance(False)
        self.PowerSignalViewAtMomentDial.setInvertedControls(False)
        self.PowerSignalViewAtMomentDial.setWrapping(False)
        self.PowerSignalViewAtMomentDial.setNotchTarget(1.0)
        self.PowerSignalViewAtMomentDial.setNotchesVisible(True)
        self.PowerSignalViewAtMomentDial.setObjectName("PowerSignalViewAtMomentDial")
        self.BackGroundImageDial = QtWidgets.QLabel(self.Principal)
        self.BackGroundImageDial.setGeometry(QtCore.QRect(750, 430, 201, 151))
        self.BackGroundImageDial.setFrameShape(QtWidgets.QFrame.Box)
        self.BackGroundImageDial.setObjectName("BackGroundImageDial")
        self.SensorViewOperation = QtWidgets.QFrame(self.Principal)
        self.SensorViewOperation.setGeometry(QtCore.QRect(20, 10, 481, 401))
        self.SensorViewOperation.setStyleSheet("background-color: rgb(118, 163, 156);")
        self.SensorViewOperation.setFrameShape(QtWidgets.QFrame.Box)
        self.SensorViewOperation.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SensorViewOperation.setObjectName("SensorViewOperation")
        self.ConfigurationButton_2 = QtWidgets.QPushButton(self.SensorViewOperation)
        self.ConfigurationButton_2.setGeometry(QtCore.QRect(110, 360, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.ConfigurationButton_2.setFont(font)
        self.ConfigurationButton_2.setStyleSheet("background-color: rgb(207, 207, 207);")
        self.ConfigurationButton_2.setObjectName("ConfigurationButton_2")
        self.gridLayoutWidget = QtWidgets.QWidget(self.SensorViewOperation)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 50, 461, 301))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.LabelM_2_1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.LabelM_2_1.setStyleSheet("background-color: rgb(162, 162, 162);")
        self.LabelM_2_1.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelM_2_1.setObjectName("LabelM_2_1")
        self.gridLayout.addWidget(self.LabelM_2_1, 2, 1, 1, 1)
        self.LabelM_1_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.LabelM_1_2.setStyleSheet("background-color: rgb(162, 162, 162);")
        self.LabelM_1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelM_1_2.setObjectName("LabelM_1_2")
        self.gridLayout.addWidget(self.LabelM_1_2, 1, 2, 1, 1)
        self.LabelM_0_0 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.LabelM_0_0.setStyleSheet("background-color: rgb(137, 255, 101);")
        self.LabelM_0_0.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelM_0_0.setObjectName("LabelM_0_0")
        self.gridLayout.addWidget(self.LabelM_0_0, 0, 0, 1, 1)
        self.LabelM_0_1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.LabelM_0_1.setStyleSheet("\n"
"background-color: rgb(162, 162, 162);")
        self.LabelM_0_1.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelM_0_1.setObjectName("LabelM_0_1")
        self.gridLayout.addWidget(self.LabelM_0_1, 0, 1, 1, 1)
        self.LabelM_0_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.LabelM_0_2.setStyleSheet("background-color: rgb(162, 162, 162);")
        self.LabelM_0_2.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelM_0_2.setObjectName("LabelM_0_2")
        self.gridLayout.addWidget(self.LabelM_0_2, 0, 2, 1, 1)
        self.LabelM_1_1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.LabelM_1_1.setStyleSheet("background-color: rgb(162, 162, 162);")
        self.LabelM_1_1.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelM_1_1.setObjectName("LabelM_1_1")
        self.gridLayout.addWidget(self.LabelM_1_1, 1, 1, 1, 1)
        self.LabelM_3_1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.LabelM_3_1.setStyleSheet("background-color: rgb(162, 162, 162);")
        self.LabelM_3_1.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelM_3_1.setObjectName("LabelM_3_1")
        self.gridLayout.addWidget(self.LabelM_3_1, 3, 1, 1, 1)
        self.LabelM_1_0 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.LabelM_1_0.setStyleSheet("background-color: rgb(137, 255, 101);")
        self.LabelM_1_0.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelM_1_0.setObjectName("LabelM_1_0")
        self.gridLayout.addWidget(self.LabelM_1_0, 1, 0, 1, 1)
        self.LabelM_3_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.LabelM_3_2.setStyleSheet("background-color: rgb(162, 162, 162);")
        self.LabelM_3_2.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelM_3_2.setObjectName("LabelM_3_2")
        self.gridLayout.addWidget(self.LabelM_3_2, 3, 2, 1, 1)
        self.LabelM_3_0 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.LabelM_3_0.setStyleSheet("background-color: rgb(137, 255, 101);")
        self.LabelM_3_0.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelM_3_0.setObjectName("LabelM_3_0")
        self.gridLayout.addWidget(self.LabelM_3_0, 3, 0, 1, 1)
        self.LabelM_2_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.LabelM_2_2.setStyleSheet("background-color: rgb(162, 162, 162);")
        self.LabelM_2_2.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelM_2_2.setObjectName("LabelM_2_2")
        self.gridLayout.addWidget(self.LabelM_2_2, 2, 2, 1, 1)
        self.LabelM_2_0 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.LabelM_2_0.setStyleSheet("background-color: rgb(137, 255, 101);")
        self.LabelM_2_0.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelM_2_0.setObjectName("LabelM_2_0")
        self.gridLayout.addWidget(self.LabelM_2_0, 2, 0, 1, 1)
        self.TerminalSerial = QtWidgets.QLabel(self.gridLayoutWidget)
        self.TerminalSerial.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.TerminalSerial.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.TerminalSerial.setObjectName("TerminalSerial")
        self.gridLayout.addWidget(self.TerminalSerial, 4, 0, 1, 3)
        self.ConfigurationButton_Start = QtWidgets.QPushButton(self.SensorViewOperation)
        self.ConfigurationButton_Start.setEnabled(False)
        self.ConfigurationButton_Start.setGeometry(QtCore.QRect(20, 360, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.ConfigurationButton_Start.setFont(font)
        self.ConfigurationButton_Start.setStyleSheet("background-color: rgb(207, 207, 207);")
        self.ConfigurationButton_Start.setObjectName("ConfigurationButton_Start")
        self.ConfigurationButton_Close = QtWidgets.QPushButton(self.SensorViewOperation)
        self.ConfigurationButton_Close.setEnabled(False)
        self.ConfigurationButton_Close.setGeometry(QtCore.QRect(380, 360, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.ConfigurationButton_Close.setFont(font)
        self.ConfigurationButton_Close.setStyleSheet("background-color: rgb(207, 207, 207);")
        self.ConfigurationButton_Close.setObjectName("ConfigurationButton_Close")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.SensorViewOperation)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 461, 41))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.SensorName = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.SensorName.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.SensorName.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.SensorName.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.SensorName.setObjectName("SensorName")
        self.gridLayout_2.addWidget(self.SensorName, 0, 0, 1, 1)
        self.Situacion = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.Situacion.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Situacion.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.Situacion.setObjectName("Situacion")
        self.gridLayout_2.addWidget(self.Situacion, 0, 1, 1, 1)
        self.Info = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.Info.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Info.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.Info.setObjectName("Info")
        self.gridLayout_2.addWidget(self.Info, 0, 2, 1, 1)
        self.PowerSignalViewGraph = PlotWidget(self.Principal)
        self.PowerSignalViewGraph.setEnabled(False)
        self.PowerSignalViewGraph.setGeometry(QtCore.QRect(20, 420, 481, 161))
        self.PowerSignalViewGraph.showGrid(x=True,y= True,alpha=0.5)
        self.PowerSignalViewGraph.setTitle("Power Signal")
        self.PowerSignalViewGraph.setYRange(10,1)
        # self.PowerSignalViewGraph.setBackground(mkColor("#F5FFFF"))
        self.PowerSignalViewGraph.setObjectName("PowerSignalViewGraph")
        self.BackGroundImageDial.raise_()
        self.CameraBox.raise_()
        self.PowerSignalViewAtMomentDial.raise_()
        self.SensorViewOperation.raise_()
        self.PowerSignalViewGraph.raise_()
        self.Pestanas.addTab(self.Principal, "")
        self.Sensores = QtWidgets.QWidget()
        self.Sensores.setStyleSheet("background-color: rgb(249, 249, 249);")
        self.Sensores.setObjectName("Sensores")


        self.Sensor0 = PlotWidget(self.Sensores)
        self.Sensor0.setEnabled(False)
        self.Sensor0.setGeometry(QtCore.QRect(40, 30, 271, 211))
        self.Sensor0.setTitle("Sensor 0")
        self.Sensor0.showGrid(x=True,y = True,alpha=0.5)
        # self.Sensor0.setBackground(mkColor("#F5FFFF"))
        self.Sensor0.setObjectName("Sensor0")

        self.Sensor1 = PlotWidget(self.Sensores)
        self.Sensor1.setEnabled(False)
        self.Sensor1.setGeometry(QtCore.QRect(400, 30, 271, 211))
        # self.Sensor1.setBackground(mkColor("#F5FFFF"))
        self.Sensor1.showGrid(x=True,y = True,alpha=0.5)
        self.Sensor1.setObjectName("Sensor1")
        self.Sensor1.setTitle("Sensor 1")
        
        self.Sensor2 = PlotWidget(self.Sensores)
        self.Sensor2.setEnabled(False)
        self.Sensor2.setGeometry(QtCore.QRect(750, 30, 271, 211))
        # self.Sensor2.setBackground(mkColor("#F5FFFF"))
        self.Sensor2.showGrid(x=True,y = True,alpha=0.5)
        self.Sensor2.setObjectName("Sensor2")
        self.Sensor2.setTitle("Sensor 2")
        
        self.Sensor3 = PlotWidget(self.Sensores)
        self.Sensor3.setEnabled(False)
        self.Sensor3.setGeometry(QtCore.QRect(40, 320, 271, 211))
        # self.Sensor3.setBackground(mkColor("#F5FFFF"))
        self.Sensor3.showGrid(x=True,y = True,alpha=0.5)
        self.Sensor3.setObjectName("Sensor3")
        self.Sensor3.setTitle("Sensor 3")
        
        self.Sensor4 = PlotWidget(self.Sensores)
        self.Sensor4.setEnabled(False)
        self.Sensor4.setGeometry(QtCore.QRect(400, 320, 271, 211))
        # self.Sensor4.setBackground(mkColor("#F5FFFF"))
        self.Sensor4.showGrid(x=True,y = True,alpha=0.5)
        self.Sensor4.setObjectName("Sensor4")
        self.Sensor4.setTitle("Sensor 4")
        
        self.Sensor5 = PlotWidget(self.Sensores)
        self.Sensor5.setEnabled(False)
        self.Sensor5.setGeometry(QtCore.QRect(760, 320, 271, 211))
        # self.Sensor5.setBackground(mkColor("#F5FFFF"))
        self.Sensor5.showGrid(x=True,y = True,alpha=0.5)
        self.Sensor5.setObjectName("Sensor5")
        self.Sensor5.setTitle("Sensor 5")



        self.pushButton = QtWidgets.QPushButton(self.Sensores)
        self.pushButton.setGeometry(QtCore.QRect(50, 550, 261, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.Sensores)
        self.pushButton_2.setGeometry(QtCore.QRect(760, 550, 261, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.Sensor1Label = QtWidgets.QLabel(self.Sensores)
        self.Sensor1Label.setGeometry(QtCore.QRect(50, 10, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Sensor1Label.setFont(font)
        self.Sensor1Label.setObjectName("Sensor1Label")
        self.Sensor2Label = QtWidgets.QLabel(self.Sensores)
        self.Sensor2Label.setGeometry(QtCore.QRect(410, 10, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Sensor2Label.setFont(font)
        self.Sensor2Label.setObjectName("Sensor2Label")
        self.Sensor3Label = QtWidgets.QLabel(self.Sensores)
        self.Sensor3Label.setGeometry(QtCore.QRect(750, 10, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Sensor3Label.setFont(font)
        self.Sensor3Label.setObjectName("Sensor3Label")
        self.Sensor4Label = QtWidgets.QLabel(self.Sensores)
        self.Sensor4Label.setGeometry(QtCore.QRect(40, 300, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Sensor4Label.setFont(font)
        self.Sensor4Label.setObjectName("Sensor4Label")
        self.Sensor5Label = QtWidgets.QLabel(self.Sensores)
        self.Sensor5Label.setGeometry(QtCore.QRect(410, 300, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Sensor5Label.setFont(font)
        self.Sensor5Label.setObjectName("Sensor5Label")
        self.Sensor6Label = QtWidgets.QLabel(self.Sensores)
        self.Sensor6Label.setGeometry(QtCore.QRect(760, 300, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Sensor6Label.setFont(font)
        self.Sensor6Label.setObjectName("Sensor6Label")
        self.Pestanas.addTab(self.Sensores, "")

        ######################################3######################################3#Visualizacion de la grafica 3D
        self.Graph3D = QtWidgets.QWidget()
        self.Graph3D.setObjectName("Graph3D")
        self.Graph3D.setStyleSheet("background-color: rgb(0, 0, 0);")
        # self.Mostrar3DGraph = QtWidgets.QPushButton(self.Graph3D)
        # self.Mostrar3DGraph.setGeometry(QtCore.QRect(40, 30, 271, 100))
        # self.Mostrar3DGraph.setText("Ver 3D")
        self.w = Visualizer(self.Graph3D)
        
        #########################################################3######################################3######################################3
        #intentamos la visualizacion grafica de los datos
        self.trace = dict()
        self.ver3D = gl.GLViewWidget(self.Graph3D)
        self.ver3D.opts['distance'] = 40
        self.ver3D.setGeometry(QtCore.QRect(10, 10, 740, 580))
        self.ver3D.setWindowTitle("Visualizacion de datos 3D")
        self.ver3D.setUpdatesEnabled(True)

        gx = gl.GLGridItem()
        gx.rotate(90, 0, 1, 0)
        gx.translate(-10, 0, 0)
        self.ver3D.addItem(gx)
        gy = gl.GLGridItem()
        gy.rotate(90, 1, 0, 0)
        gy.translate(0, -10, 0)
        self.ver3D.addItem(gy)
        gz = gl.GLGridItem()
        gz.translate(0, 0, -10)
        self.ver3D.addItem(gz)

        self.n = 60
        self.m = 1000
        self.y = np.linspace(-10, 10, self.n)
        self.x = np.linspace(-10, 10, self.m)
        self.phase = 0

        for i in range(self.n):
            yi = np.array([self.y[i]] * self.m)
            d = np.sqrt(self.x ** 2 + yi ** 2)
            z = 10 * np.cos(d + self.phase) / (d + 1)
            pts = np.vstack([self.x, yi, z]).transpose()
            self.trace[i] = gl.GLLinePlotItem(pos=pts, color=pg.glColor(
                (i, self.n * 1.3)), width=(i + 1) / 10, antialias=True)
            self.ver3D.addItem(self.trace[i])

    
        ######################################3######################################3######################################3
        self.Pestanas.addTab(self.Graph3D, "")
        ######################################3######################################3#Termina la seccionde la graficacion 3D

        self.Bibliografia = QtWidgets.QWidget()
        self.Bibliografia.setObjectName("Bibliografia")
        self.frame_3 = QtWidgets.QFrame(self.Bibliografia)
        self.frame_3.setGeometry(QtCore.QRect(20, 40, 971, 161))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_3.setLineWidth(1)
        self.frame_3.setMidLineWidth(0)
        self.frame_3.setObjectName("frame_3")
        self.label_7 = QtWidgets.QLabel(self.frame_3)
        self.label_7.setGeometry(QtCore.QRect(10, 10, 161, 141))
        self.label_7.setFrameShape(QtWidgets.QFrame.Box)
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("Cony.jpg"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.frame_3)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(190, 10, 741, 141))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_2.addWidget(self.label_13)
        self.label_14 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_2.addWidget(self.label_14)
        self.label_15 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_2.addWidget(self.label_15)
        self.frame_4 = QtWidgets.QFrame(self.Bibliografia)
        self.frame_4.setGeometry(QtCore.QRect(20, 230, 971, 161))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_4.setLineWidth(1)
        self.frame_4.setMidLineWidth(0)
        self.frame_4.setObjectName("frame_4")
        self.label_8 = QtWidgets.QLabel(self.frame_4)
        self.label_8.setGeometry(QtCore.QRect(770, 10, 191, 141))
        self.label_8.setFrameShape(QtWidgets.QFrame.Box)
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("CarlosAdrian.jpeg"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.frame_4)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 741, 141))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_19 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_4.addWidget(self.label_19)
        font.setPointSize(12)
        self.label_20 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        
        self.verticalLayout_4.addWidget(self.label_20)
        font.setPointSize(12)
        self.label_21 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_4.addWidget(self.label_21)
        self.frame_5 = QtWidgets.QFrame(self.Bibliografia)
        self.frame_5.setGeometry(QtCore.QRect(20, 420, 971, 161))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_5.setLineWidth(1)
        self.frame_5.setMidLineWidth(0)
        self.frame_5.setObjectName("frame_5")
        self.label_9 = QtWidgets.QLabel(self.frame_5)
        self.label_9.setGeometry(QtCore.QRect(10, 10, 161, 141))
        self.label_9.setFrameShape(QtWidgets.QFrame.Box)
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("Emmanuel.jpg"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.frame_5)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(180, 10, 741, 141))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_22 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_5.addWidget(self.label_22)
        self.label_23 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.verticalLayout_5.addWidget(self.label_23)
        font.setPointSize(12)
        self.label_24 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.verticalLayout_5.addWidget(self.label_24)
        self.label_10 = QtWidgets.QLabel(self.Bibliografia)
        self.label_10.setGeometry(QtCore.QRect(20, 10, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.Pestanas.addTab(self.Bibliografia, "")
        self.TituloProyecto = QtWidgets.QLabel(self.centralwidget)
        self.TituloProyecto.setGeometry(QtCore.QRect(10, 20, 911, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.TituloProyecto.setFont(font)
        self.TituloProyecto.setToolTip("")
        self.TituloProyecto.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.TituloProyecto.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.TituloProyecto.setLineWidth(0)
        self.TituloProyecto.setObjectName("TituloProyecto")
        self.ImagenSupIzq = QtWidgets.QLabel(self.centralwidget)
        self.ImagenSupIzq.setGeometry(QtCore.QRect(960, 0, 91, 91))
        self.ImagenSupIzq.setText("")
        self.ImagenSupIzq.setPixmap(QtGui.QPixmap("UdeGSPACE.png"))
        self.ImagenSupIzq.setScaledContents(True)
        self.ImagenSupIzq.setObjectName("ImagenSupIzq")
        ModularProject.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ModularProject)
        self.statusbar.setEnabled(True)
        self.statusbar.setSizeGripEnabled(True)
        self.statusbar.setObjectName("statusbar")
        ModularProject.setStatusBar(self.statusbar)

        #self.CameraConfigurationSetUpClass = CameraThread("http://192.168.31.32:8080/video")
        # self.CameraConfigurationSetUpClass = CameraThread(0)
        # self.CameraConfigurationSetUpClass.start()

        #Agregamos el modulo Qtimer para la actualizacion peridodica de los datos:
        self.PeriodicUpdate = QtCore.QTimer()
        self.PeriodicUpdate.setInterval(20)
        self.PeriodicUpdate.timeout.connect(self.ContinueUpdate)
        self.PeriodicUpdate.start()

        self.retranslateUi(ModularProject)
        self.Pestanas.setCurrentIndex(0)
        self.ConfigurationButton_Start.clicked.connect(self.ChangeOfColorGreen)
        self.ConfigurationButton_Close.clicked.connect(self.ChangeOfColorRed)
        # self.ConfigurationButton.clicked.connect(self.ConfigurationButton.update)
        self.ConfigurationButton_2.clicked.connect(self.SerialConfigurationSetUp)
        self.ConfigurationButton.clicked.connect(self.lineEdit.copy)
        # self.CameraConfigurationSetUpClass.ImageUpdate.connect(self.imageUpdateSlot)

        
        self.pushButton.clicked.connect(lambda:self.draw())
        self.pushButton_2.clicked.connect(lambda:self.clear())
        # self.Mostrar3DGraph.clicked.connect(self.mostrar3dclass)
        QtCore.QMetaObject.connectSlotsByName(ModularProject)
        

    def ContinueUpdate(self):
        self.w.update()
        # self.update3DGraph()
        self.LoopCount = self.LoopCount + 1
        self.countLoop = self.countLoop + 1
        if self.LoopCount == 50 or self.LoopCount == 100:
            # self.LoopCount = 0
            self.draw()
        elif self.countLoop == 200:
            self.countLoop = 0
            self.LoopCount = 0
            self.clear()

    def draw(self):
        x = np.random.normal(size=10)
        y = np.random.normal(size=(3,10))

        fs = 500
        f = random.randint(1,100)
        ts = 1/fs
        lengtOFSignal = 100
        t = np.linspace(0,100,lengtOFSignal)

        cossignal = np.cos(2*np.pi*f*t)

        
        for i in range(3):
            # self.Sensor0.plot(x,y[i],pen=(i,3))
            self.Sensor0.plot(t,cossignal,pen='r')
            self.Sensor1.plot(x,y[i],pen=(i,3))
            self.Sensor2.plot(x,y[i],pen=(i,3))
            self.Sensor3.plot(x,y[i],pen=(i,3))
            self.Sensor4.plot(x,y[i],pen=(i,3))
            # self.Sensor5.plot(x,y[i],pen=(i,3))
            self.PowerSignalViewGraph.plot(t,cossignal+7,pen='w')

    def clear(self):
        self.Sensor0.clear()
        self.Sensor1.clear()
        self.Sensor2.clear()
        self.Sensor3.clear()
        self.Sensor4.clear()
        # self.Sensor5.clear()
        self.PowerSignalViewGraph.clear()
    # def mostrar3dclass(self):
    #     v = Visualizer()
    #     v.animation()
    
    def ChangeOfColorGreen(self):
        self.LabelM_0_1.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.LabelM_1_1.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.LabelM_2_1.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.LabelM_3_1.setStyleSheet("background-color: rgb(0, 255, 0);")
        
        # SerialConfigurationtxt = open("SerialConfiguration.txt","r")
        # listInfo = SerialConfigurationtxt.readlines()            
        # SerialConfigurationtxt.close()
        # self.SerialData = SeparaLista(listInfo[0],',')
        # mensaje = "Puerto:" + str(self.SerialData[0]) + "\nBaudrate:" + str(self.SerialData[1]) + "\nBytesize:" + str(self.SerialData[2]) + "\nParity:" + str(self.SerialData[3]) 
        # self.TerminalSerial.setText(mensaje)
        # self.PuertoSerialopen = serial.Serial(port=self.SerialData[0],baudrate=int(self.SerialData[1]))
        
       
    def ChangeOfColorRed(self):
        self.LabelM_0_1.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.LabelM_1_1.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.LabelM_2_1.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.LabelM_3_1.setStyleSheet("background-color: rgb(255, 0, 0);")
    def SerialConfigurationSetUp(self):
        self.ConfigurationButton_Start.setEnabled(True)
        self.ConfigurationButton_Close.setEnabled(True)

        self.SerialConfigurationFrame = QtWidgets.QFrame()
        self.SetUpUISerialConfiguration = Ui_SerialConfiguration()
        self.SetUpUISerialConfiguration.setupUi(self.SerialConfigurationFrame)
        self.SerialConfigurationFrame.show()


    def imageUpdateSlot(self,ImageCamera):
        self.CameraImage.setPixmap(QtGui.QPixmap.fromImage(ImageCamera))

    # def GetDataFrameSerial(self):
    #     hola =  self.PuertoSerialopen.read_all()
    #     hola =hola.decode('utf-8')
    #     print(str(hola))

    def retranslateUi(self, ModularProject):
        _translate = QtCore.QCoreApplication.translate
        ModularProject.setWindowTitle(_translate("ModularProject", "MainWindow"))
        self.ConfigurationButton.setText(_translate("ModularProject", "Start"))
        self.BackGroundImageDial.setText(_translate("ModularProject", "TextLabel"))
        self.ConfigurationButton_2.setText(_translate("ModularProject", "Serial Port Configuration "))
        self.LabelM_2_1.setText(_translate("ModularProject", "###"))
        self.LabelM_1_2.setText(_translate("ModularProject", "###"))
        self.LabelM_0_0.setText(_translate("ModularProject", "MPU9250"))
        self.LabelM_0_1.setText(_translate("ModularProject", "###"))
        self.LabelM_0_2.setText(_translate("ModularProject", "###"))
        self.LabelM_1_1.setText(_translate("ModularProject", "###"))
        self.LabelM_3_1.setText(_translate("ModularProject", "###"))
        self.LabelM_1_0.setText(_translate("ModularProject", "GPS"))
        self.LabelM_3_2.setText(_translate("ModularProject", "###"))
        self.LabelM_3_0.setText(_translate("ModularProject", "Temperartura"))
        self.LabelM_2_2.setText(_translate("ModularProject", "###"))
        self.LabelM_2_0.setText(_translate("ModularProject", "BMP280"))
        self.TerminalSerial.setText(_translate("ModularProject", "Terminal"))
        self.ConfigurationButton_Start.setText(_translate("ModularProject", "Start"))
        self.ConfigurationButton_Close.setText(_translate("ModularProject", "Close"))
        self.SensorName.setText(_translate("ModularProject", "Name:"))
        self.Situacion.setText(_translate("ModularProject", "Active?:"))
        self.Info.setText(_translate("ModularProject", "Situation or state:"))
        self.Pestanas.setTabText(self.Pestanas.indexOf(self.Principal), _translate("ModularProject", "Principal"))
        self.pushButton.setText(_translate("ModularProject", "Show"))
        self.pushButton_2.setText(_translate("ModularProject", "Clear"))
        self.Sensor1Label.setText(_translate("ModularProject", "Sensor 1"))
        self.Sensor2Label.setText(_translate("ModularProject", "Sensor 2"))
        self.Sensor3Label.setText(_translate("ModularProject", "Sensor 3"))
        self.Sensor4Label.setText(_translate("ModularProject", "Sensor 4"))
        self.Sensor5Label.setText(_translate("ModularProject", "Sensor 5"))
        self.Sensor6Label.setText(_translate("ModularProject", "Sensor 6"))
        self.Pestanas.setTabText(self.Pestanas.indexOf(self.Sensores), _translate("ModularProject", "Sensores"))
        self.Pestanas.setTabText(self.Pestanas.indexOf(self.Graph3D), _translate("ModularProject", "Graph3D"))

        ############################# Informacion de Cony ###################################################################################
        self.label_13.setText(_translate("ModularProject", "Nombre: Maria Concepcion Sandoval Becerra "))
        self.label_14.setText(_translate("ModularProject", "C??digo:216342157"))
        self.label_15.setText(_translate("ModularProject", "Descripci??n: Estudiante actual de la carrera de comunicaciones "\
                                        "y electronica, encargada de la creacion del prototipo en el cual\n "\
                                        "estaran montados los sensores y donde se haran pruebas de posicionamiento en conjunto de las antena,"  \
                                        "dise??o y prototipado \nminimo en tarjetas electronicas"))
        #######################################################################################################################################

        ############################# Informacion de Carlos ###################################################################################
        self.label_19.setText(_translate("ModularProject", "Nombre: Carlos Adrian Garc??a Zambrano"))
        self.label_20.setText(_translate("ModularProject", "C??digo:  209618104"))
        self.label_21.setText(_translate("ModularProject", "Descripci??n: Mi participaci??n ha sido la busqueda e implemetaci??n de soluciones para"\
                                                        " los problemas que\n nos enfrentamos, dentro de estas, encontramos principalmente con el "\
                                                        "analisis de circuitos\n y de la creacion de hardware, asi como de los calculos fisicos y/o mecanicos"))
        #########################################################################################################################################

        ############################# Informacion de Emmanuel ###################################################################################
        self.label_22.setText(_translate("ModularProject", "Nombre:Emmanuel Paredes Camargo "))
        self.label_23.setText(_translate("ModularProject", "C??digo:215038166"))
        self.label_24.setText(_translate("ModularProject", "Descripci??n: Mi participaci??n se centro en el dise??o, desarrollo e implementaci??n de "\
                                        "la interfaz grafica\n y programas usados en los microcontroladores, ademas del tratamiento aplicado a las "\
                                        " tramas de \ninformacion, as?? como de su debida asignacion dentro de los programas"))
        #########################################################################################################################################

        self.label_10.setText(_translate("ModularProject", "Integrantes:"))
        self.Pestanas.setTabText(self.Pestanas.indexOf(self.Bibliografia), _translate("ModularProject", "Bibliografia"))
        self.TituloProyecto.setText(_translate("ModularProject", "Proyecto Modular :Control de navegacion inteligente para robot de exproracion espacial "))
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ModularProject = QtWidgets.QMainWindow()
    ui = Ui_ModularProject()
    ui.setupUi(ModularProject)
    ModularProject.show()
    sys.exit(app.exec_())
