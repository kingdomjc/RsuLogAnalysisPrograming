# coding=utf-8
import time
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


class ResultFormat:
    @classmethod
    def printResult(cls, analysis, target):
        target.textBrowser.append(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ":")
        target.textBrowser.append("*" * 80)
        target.textBrowser.append(u"    源日志: " + target.originFileName)
        target.textBrowser.append("*" * 80)
        target.textBrowser.append(u"被检测日志: " + target.checkFileName)
        target.textBrowser.append("*" * 80)
        target.textBrowser.append(u"  检测数量：" + str(analysis.total))
        target.textBrowser.append("*" * 80)
        target.textBrowser.append(u"  正确数量：" + str(analysis.findNum) + "\n")
        target.textBrowser.append("*" * 80)
        target.textBrowser.append(u"    正确率：" + str(float(analysis.findNum) / analysis.total))
        target.textBrowser.append("*" * 80)
        target.textBrowser.append(u"  源文件未正确的：")
        for key in analysis.NoSuccessSor:
            target.textBrowser.append(str(key))
        target.textBrowser.append("*" * 80)
        target.textBrowser.append(u"  找到但是未正确的：")
        for key in analysis.NoFind:
            target.textBrowser.append(str(key))
        target.textBrowser.append("*" * 80)
        target.textBrowser.append(u"    成功率：" + str(float(analysis.successNum) / analysis.total))
        target.textBrowser.append("*" * 80)
        target.textBrowser.append(u"  未成功的：")
        for key in analysis.NoSuccess.keys():
            target.textBrowser.append(key + ": ")
            for value in analysis.NoSuccess[key]:
                target.textBrowser.append(" " * (len(key) + 1) + value)
            target.textBrowser.append("_" * 40)
        target.textBrowser.append("*" * 80)
        target.textBrowser.append(u"需要人工检测:")
        for key in analysis.manualDetection:
            target.textBrowser.append(str(key))
        target.textBrowser.append("*" * 80)
        target.textBrowser.append(u"  车型信息：")
        for key in analysis.carMode.keys():
            target.textBrowser.append(u"    车型" + str(key) + ": " + u"数量：" + str(analysis.carMode[key]))

    @classmethod
    def printBar(cls, s):
        print s
