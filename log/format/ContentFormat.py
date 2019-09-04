# coding=utf-8

import re
import time
from log.entity.DeductCostEntity import DeductCostEntity


class ContentFormat:
    regex = {0: ".*入口站:3600517.*",
             1: ".*OBUID:.*",
             2: "OBUID:",
             3: ",",
             4: ".*车型.*",
             5: "车型:",
             6: ":  ",
             7: ".*交易成功.*",
             8: ""
             }

    def __init__(self):
        # 组转完成之后的内容，为DeductCost模型
        self.__content = []

    def formatThey(self, window, content):
        i = 0
        content = content.split("\n")
        for s in content:
            if re.search(self.regex[0], s) is not None:
                aData = DeductCostEntity()
                for j in range(i + 14, i - 13, -1):
                    if j <= i:
                        line = re.search(self.regex[1], content[j])
                        if line is not None:
                            usefulContent = line.group()
                            aData.setTime(usefulContent[0:23])
                            aData.setObuId(usefulContent.split(self.regex[2])[1].split(self.regex[3])[0])
                            break
                        elif re.search(self.regex[4], content[j]) is not None:
                            aData.setCarModel(content[j].split(self.regex[5])[1].split(self.regex[3])[0])
                    elif re.search(self.regex[7], content[j]) is not None:
                        aData.setStatus(1)
                if not self.__content.__contains__(aData):
                    self.__content.append(aData)
            i = i + 1
        window.setProgressValue((i / len(content)) * 100)
        return self.__content

    def formatOurs(self, window, content):
        content = content.split("\n")
        i = 0
        for i in range(0, len(content)):
            searchObuId = re.search(self.regex[1], content[i])
            if searchObuId is not None:
                aData = DeductCostEntity()
                usefulContent = searchObuId.group()
                aData.setTime(usefulContent[0:23])
                aData.setObuId(usefulContent.split(self.regex[2])[1].split(self.regex[3])[0])
                for j in range(i, len(content)):
                    noneLine = content[j].split(self.regex[6])
                    if content[j] == "" or (len(noneLine) > 1 and noneLine[1] == ""):
                        searchStatus = re.search(self.regex[7], content[j - 1])
                        if searchStatus is not None:
                            aData.setStatus(1)
                        else:
                            aData.setStatus(0)
                            aData.setErrorInfo(
                                unicode(content[j - 1].split(self.regex[6])[1], "utf-8"))
                        i = j
                        break
                    j += 1
                self.__content.append(aData)
            i = i + 1
            window.setProgressValue((float(i) / len(content)) * 100)
        window.textBrowser.append(time.strftime("%Y-%m-%d %H:%M:%S",
                                                time.localtime()) + "  " + u"读取检测文件完成")
        window.thread2 = None
        window.checkContent = self.__content
        return u"完成"
