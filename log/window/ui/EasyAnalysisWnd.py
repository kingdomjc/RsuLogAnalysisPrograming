# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EasyAnalysis.ui'
#
# Created: Fri Aug 23 15:02:02 2019
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(776, 535)
        MainWindow.setStyleSheet(_fromUtf8("*{\n"
"    font-size:13pt\n"
"}"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(28, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.originalLog = QtGui.QPushButton(self.centralwidget)
        self.originalLog.setObjectName(_fromUtf8("originalLog"))
        self.horizontalLayout.addWidget(self.originalLog)
        self.checkLog = QtGui.QPushButton(self.centralwidget)
        self.checkLog.setObjectName(_fromUtf8("checkLog"))
        self.horizontalLayout.addWidget(self.checkLog)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.analysisLog = QtGui.QPushButton(self.centralwidget)
        self.analysisLog.setObjectName(_fromUtf8("analysisLog"))
        self.horizontalLayout.addWidget(self.analysisLog)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.clearLog = QtGui.QPushButton(self.centralwidget)
        self.clearLog.setObjectName(_fromUtf8("clearLog"))
        self.horizontalLayout.addWidget(self.clearLog)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setProperty(_fromUtf8("value"), 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.gridLayout.addWidget(self.progressBar, 1, 0, 1, 1)
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setOverwriteMode(True)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.gridLayout.addWidget(self.textBrowser, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 776, 28))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.originalLog.setText(QtGui.QApplication.translate("MainWindow", "源日志", None, QtGui.QApplication.UnicodeUTF8))
        self.checkLog.setText(QtGui.QApplication.translate("MainWindow", "待检测日志", None, QtGui.QApplication.UnicodeUTF8))
        self.analysisLog.setText(QtGui.QApplication.translate("MainWindow", "分析日志", None, QtGui.QApplication.UnicodeUTF8))
        self.clearLog.setText(QtGui.QApplication.translate("MainWindow", "清除内容", None, QtGui.QApplication.UnicodeUTF8))

