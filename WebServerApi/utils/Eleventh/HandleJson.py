# coding=utf-8
import utils.Eleventh.ReadFromES as ReadFromES
from utils.First.HandleTime import HandleTime

class Handler:
    def __init__(self, province, startMonth, endMonth,range):
        self.province = province
        self.startMonth = startMonth
        self.endMonth = endMonth
        self.range=range

    def getDataFromServer(self):
        connect = ReadFromES.scan_data_fun()
        self.handle = HandleTime(self.startMonth, self.endMonth)
        self.time = self.handle.handle()

        List = []
        for i in self.time:
            Data, isTrue = connect.get_battery_data(self.province, i[0], i[1],self.range)
            if isTrue == False:
                return [], False
            List.append(self.computeResult(Data, i))
        return List, True

    def computeResult(self, data, time):
        jj = dict()
        jj["month"] = self.handle.reversehandle(time[1])
        value=0
        for i in data:
            if i.charge_times_eachday!='-32000' and i.charge_times_eachday!='-32000.0':
                value+=float(i.charge_times_eachday)

        jj["value"]=value
        return jj
