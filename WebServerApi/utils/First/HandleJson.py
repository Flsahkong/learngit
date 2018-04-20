# coding=utf-8
import utils.First.ReadFromES as ReadFromES
from utils.First.HandleTime import HandleTime


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
        high, low, normal = 0, 0, 0
        for i in data:
            if i.T_charge_model == '慢充':
                low += 1
            elif i.T_charge_model == '快充':
                high += 1
            else:
                normal += 1
        jj['fastChargeNum'] = int(normal / 2) + high
        jj['slowChargeNum'] = int(normal / 2) + low
        return jj
