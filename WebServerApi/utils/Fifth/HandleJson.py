# coding=utf-8
from utils.First.HandleTime import HandleTime
import utils.Fifth.ReadFromES as ReadFromES


class Handler:
    def __init__(self, province, startMonth, endMonth):
        self.province = province
        self.startMonth = startMonth
        self.endMonth = endMonth

    def getDataFromServer(self):
        connect = ReadFromES.scan_data_fun()
        self.handle = HandleTime(self.startMonth, self.endMonth)
        self.time = self.handle.handle()
        List = []
        for i in self.time:
            Data, isTrue = connect.get_battery_data(self.province, i[0], i[1])
            if isTrue == False:
                return [], False
            List.append(self.computeResult(Data, i))
        return List, True

    def computeResult(self, data, time):
        jj = dict()
        jj["month"] = self.handle.reversehandle(time[0])
        value = 0
        for i in data:
            if i[0] == '-32000' or i[0] == '-32000.0':
                a = 0
            else:
                a = float(i[0])
            if i[1] == '-32000' or i[1] == '-32000.0':
                b = 0
            else:
                b = float(i[1])
            value += a * b * int(i[2])
        jj['value'] = value
        return jj
