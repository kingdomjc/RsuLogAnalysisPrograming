# coding=utf-8
import sys
import thread
import time
from functools import partial

from PyQt4.QtCore import pyqtSignal, SIGNAL
from PyQt4.QtGui import *
from PyQt4 import QtCore, QtGui

from log.analysis.AnalysisLog import AnalysisLog
from log.format.ContentFormat import ContentFormat
from log.format.ReasultFormat import ResultFormat
from log.operatfile.FileOperate import FileOperate
from log.window.ui.EasyAnalysisWnd import Ui_MainWindow


class WndLogic(QMainWindow, Ui_MainWindow):
    error = pyqtSignal()

    def __init__(self, parent=None):
        super(WndLogic, self).__init__(parent)
        self.setupUi(self)
        self.originalLog.clicked.connect(self.getOriginalFile)
        self.checkLog.clicked.connect(self.getCheckFile)
        self.analysisLog.clicked.connect(self.analysis)
        self.clearLog.clicked.connect(self.clearLogPrg)
        self.error.connect(self.errorHandler)
        self.connect(self, SIGNAL("result"),
                     ResultFormat.printResult)
        self.connect(self, SIGNAL("format"), ResultFormat.printBar)
        self.progressBar.setValue(0)

        # 源日志
        self.originContent = None
        # 被检测的日志模型
        self.checkContent = None

        self.originFileName = None
        self.checkFileName = None
        self.thread1 = None
        self.thread2 = None

    def getOriginalFile(self):
        if self.thread1 is not None:
            QMessageBox.about(None, u"提示", u"分析工具已经启动")
        else:
            self.progressBar.setValue(0)
            filename = QtGui.QFileDialog.getOpenFileName(self, u'选择文件', '/').__str__()
            if filename is not None and filename is not u'':
                self.originContent = None
                self.originFileName = None
                theyFile = FileOperate(filename)
                theyFormat = ContentFormat()
                self.originContent = theyFormat.formatThey(self, theyFile.content)
                self.originFileName = filename.split("/")[-1]
                self.textBrowser.append(time.strftime("%Y-%m-%d %H:%M:%S",
                                                      time.localtime()) + "  " + u"读取源文件完成")

    def getCheckFile(self):
        if self.thread1 is not None:
            QMessageBox.about(None, u"提示", u"分析工具已经启动")
        elif self.thread2 is not None:
            QMessageBox.about(None, u"提示", u"正在加载")
        else:
            self.progressBar.setValue(0)
            filename = QtGui.QFileDialog.getOpenFileName(self, u'选择文件', '/').__str__()
            if filename is not None and filename is not u'':
                self.checkContent = None
                self.checkFileName = None
                ourFile = FileOperate(filename)
                ourFormat = ContentFormat()
                self.checkFileName = filename.split("/")[-1]
                self.thread2 = thread.start_new_thread(self.checkTask, (ourFormat, ourFile,))

    def checkTask(self, ourFormat, ourFile):
        try:
            self.emit(SIGNAL("format"), ourFormat.formatOurs(self, ourFile.content))
        except:
            QMessageBox.about(None, u"错误", u"文件不匹配")
            self.thread2 = None

    def analysis(self):
        if self.thread1 is not None:
            QMessageBox.about(None, u"提示", u"分析工具已经启动")
        elif self.thread2 is not None or self.originContent is None:
            QMessageBox.about(None, u"提示", u"请将文件加载完成")
        else:
            self.thread1 = thread.start_new_thread(self.analysisTask, ())

    def clearLogPrg(self):
        self.textBrowser.clear()

    def analysisTask(self):
        try:
            self.progressBar.setValue(0)
            ana = AnalysisLog()
            self.emit(SIGNAL("result"), ana.calculating(self, self.originContent, self.checkContent), self)
            self.thread1 = None
        except:
            print "抓取到了异常"
            self.error.emit()

    def run(self):
        self.show()

    def errorHandler(self):
        self.originContent = None
        self.checkContent = None
        self.thread1 = None
        self.originFileName = None
        self.checkFileName = None
        QMessageBox.about(None, u"错误", u"操作错误")

    def setProgressValue(self, value):
        self.progressBar.setValue(value)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = WndLogic()
    window.run()
    sys.exit(app.exec_())
