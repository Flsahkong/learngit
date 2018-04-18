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
        jj["month"] = self.handle.reversehandle(time[1])
        value = 0
        for i in data:
            if i.charge_ah_aver == '-32000' or i.charge_ah_aver == '-32000.0':
                a = 0
            else:
                a = float(i.charge_ah_aver)
            if i.charge_times_eachday == '-32000' or i.charge_times_eachday == '-32000.0':
                b = 0
            else:
                b = float(i.charge_times_eachday)
            value += a * b
        jj['value'] = value
        return jj
