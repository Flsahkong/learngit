# coding=utf-8
from utils.First.HandleTime import HandleTime
import utils.Third.ReadFromES as ReadFromES


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
        charge_time_each = 0
        for i in data:
            if i[0] != '-32000' and i[0] != '-32000.0':
                charge_time_each += float(i[0])*float(i[1])
        jj['value'] = charge_time_each
        return jj
