# coding=utf-8
from time import strptime, mktime, localtime, strftime


class DeductCostEntity:
    def __init__(self):
        self.__time = None
        self.__obuId = None
        self.__carModel = None
        self.__status = None
        self.__errorInfo = None

    def setTime(self, time):
        if isinstance(time, str):
            time = strptime(time, '%Y-%m-%d %H:%M:%S.%f')
            time = int(mktime(time))
        self.__time = time

    def getTime(self):
        if self.__time is not None:
            return self.__time
        else:
            return ""

    def setObuId(self, obuId):
        self.__obuId = obuId

    def getObuId(self):
        if self.__obuId is not None:
            return self.__obuId
        else:
            return ""

    def setCarModel(self, carModel):
        self.__carModel = carModel

    def getCarModel(self):
        if self.__carModel is not None:
            return self.__carModel
        else:
            return ""

    def setStatus(self, status):
        self.__status = status

    def getStatus(self):
        if self.__status is not None:
            return self.__status
        else:
            return ""

    def setErrorInfo(self, errorInfo):
        self.__errorInfo = errorInfo

    def getErrorInfo(self):
        if self.__errorInfo is not None:
            return self.__errorInfo
        else:
            return ""

    def __str__(self):
        timeArray = localtime(self.getTime())
        otherStyleTime = strftime("%Y-%m-%d %H:%M:%S", timeArray)
        return " " * 11 + "Time:" + otherStyleTime + "\n" + \
               " " * 11 + "obuId:" + self.getObuId() + "\n"


if __name__ == "__main__":
    entity = DeductCostEntity()
    entity.setTime("2019-08-21 00:00:14.546")
    unit = 3600 * 24
    date_stamp = (entity.getTime() - ((entity.getTime() + (8 * 3600)) % unit))
    timeArray = localtime(date_stamp)
    otherStyleTime = strftime("%Y-%m-%d %H:%M:%S", timeArray)
    print otherStyleTime
