# coding=utf-8
import re
from time import localtime, strftime


class AnalysisLog:
    logTimeDiff = 6 * 60

    def __init__(self):
        # 没有找到的
        self.NoFind = []
        # 找到的数目
        self.findNum = 0
        # 源日志中的所有要检查的数目
        self.total = None
        # 成功的数目
        self.successNum = 0
        # 没有成功的
        self.NoSuccess = {}
        # 车型统计
        self.carMode = {}
        # 需要人工检查的
        self.manualDetection = []

    # def calculatingFindRate(self, window, source, checked):
    #     findNum = 0
    #     successNum = 0
    #     bar = 0  # 用于界面进度条
    #     for s in source:
    #         for t in range(len(checked)):
    #             if re.search(".*" + s + ".*", checked[t]) is not None:
    #                 findNum += 1
    #                 print findNum
    #                 if re.search(".*交易成功.*", checked[t + 1]) is not None:
    #                     successNum += 1
    #                 elif re.search(".*余额不足.*", checked[t + 1]) is not None:
    #                     successNum += 1
    #                     self.creditLower.append(s)
    #                 else:
    #                     self.NoSuccess.append(s)
    #                     errorLine = re.search(".*错误代码.*", checked[t + 1])
    #                     if errorLine is not None:
    #                         code = errorLine.group().split("错误代码")[1].split("：")[1]
    #                         if self.errorCode.get(code) is not None:
    #                             self.errorCode.get(code).append(s)
    #                         else:
    #                             self.errorCode[code] = [s]
    #                 break
    #             elif t == len(checked) - 1:
    #                 self.NoFind.append(s)
    #         bar += 1
    #         window.setProgressValue(float(bar) / len(source) * 100)
    #     return findNum, successNum, self.NoFind, self.NoSuccess, self.creditLower, self.errorCode

    def calculating(self, window, source, checked):
        bar = 0
        self.total = len(source)
        source = self.__filter(source)
        for a in source:
            start = a.getTime() - self.logTimeDiff
            end = a.getTime() + self.logTimeDiff
            self.__setCarModel(a)
            tChecked = self.__slitByTime(checked, start, end, a)
            self.__success(tChecked)
            self.__noSuccess(tChecked)
            bar += 1
            window.setProgressValue(float(bar) / len(source) * 100)
        return self

    def __success(self, tChecked):
        if tChecked is not None and tChecked[-1].getStatus() == 1:
            self.successNum += 1

    def __noSuccess(self, tChecked):
        if tChecked is not None and tChecked[-1].getStatus() == 0:
            nsInfo = tChecked[-1].getErrorInfo()
            nsId = tChecked[-1].getObuId()
            if self.NoSuccess.get(nsInfo) is not None:
                self.NoSuccess.get(nsInfo).append(nsId)
            else:
                self.NoSuccess[nsInfo] = [nsId]

    def __slitByTime(self, checked, start, end, a):
        tChecked = []
        sIndex = self.__twoPointLookup(checked, start)
        eIndex = self.__twoPointLookup(checked, end)

        for b in range(sIndex, eIndex):
            if checked[b].getTime() in range(start, end) and a.getObuId() == checked[b].getObuId():
                if len(tChecked) != 0:
                    tChecked[0].setTime(checked[b].getTime())
                    tChecked[0].setStatus(checked[b].getStatus())
                    tChecked[0].setErrorInfo(checked[b].getErrorInfo())
                    continue
                else:
                    self.findNum += 1
                    tChecked.append(checked[b])
        if len(tChecked) == 0:
            self.NoFind.append(a)
        else:
            return tChecked

    def __twoPointLookup(self, checked, key):
        i = len(checked)
        low = 0
        high = len(checked) - 1
        mid = None
        while low <= high:
            mid = (low + high) / 2
            if key < checked[mid].getTime():
                high = mid - 1
            elif key > checked[mid].getTime():
                low = mid + 1
            else:
                return mid
        return mid

    def __setCarModel(self, a):
        if self.carMode.get(a.getCarModel()) is None:
            self.carMode[a.getCarModel()] = 1
        else:
            self.carMode[a.getCarModel()] = self.carMode.get(a.getCarModel()) + 1

    def __filter(self, source):
        index = self.__twoPointLookup(source, source[0].getTime() + self.logTimeDiff)
        self.manualDetection = source[0:index]
        return source[index:len(source)]
