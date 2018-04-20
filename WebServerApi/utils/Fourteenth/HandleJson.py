# coding=utf-8
import utils.Fourteenth.ReadFromES as ReadFromES
from utils.First.HandleTime import HandleTime


class Handler:
    def __init__(self, province, startMonth, endMonth, vehicletype):
        self.province = province
        self.startMonth = startMonth
        self.endMonth = endMonth
        self.vehicletype = vehicletype

    def getDataFromServer(self):
        connect = ReadFromES.scan_data_fun()
        self.handle = HandleTime(self.startMonth, self.endMonth)
        self.time = self.handle.handle()

        List = []
        for i in self.time:
            Data, isTrue = connect.get_battery_data(self.province, i[0], i[1], vehicletype=self.vehicletype)
            if isTrue == False:
                return [], False
            List.append(self.computeResult(Data, i))
        return List, True

    def computeResult(self, data, time):
        jj = dict()
        jj["month"] = self.handle.reversehandle(time[0])

        a = list()
        temp = dict()
        for i in data:
            if temp.has_key("%s" % i.BatteryHealth_Range):
                temp["%s" % i.BatteryHealth_Range] += 1
            else:
                temp["%s" % i.BatteryHealth_Range] = 1
        for key,value in temp.items():
            a.append({"healthScoreRange":key,"vehicleNum":value})

        jj["range_data"]=a
        return jj