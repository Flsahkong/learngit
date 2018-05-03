# coding=utf-8
import utils.Twelfth.ReadFromES as ReadFromES
from utils.First.HandleTime import HandleTime


class Handler:
    def __init__(self, province, startMonth, endMonth, range):
        self.province = province
        self.startMonth = startMonth
        self.endMonth = endMonth
        self.range = range

    def getDataFromServer(self):
        connect = ReadFromES.scan_data_fun()
        self.handle = HandleTime(self.startMonth, self.endMonth)
        self.time = self.handle.handle()

        List = []
        for i in self.time:
            Data, isTrue = connect.get_battery_data(self.province, i[0], i[1], self.range)
            if isTrue == False:
                return [], False
            List.append(self.computeResult(Data, i))
        return List, True

    def computeResult(self, data, time):
        jj = dict()
        jj["month"] = self.handle.reversehandle(time[0])
        value = 0
        for i in data:
            if i[0] != '-32000' and i[0] != '-32000.0':
                value += float(i[0])*int(i[1])

        jj["value"] = value
        return jj
