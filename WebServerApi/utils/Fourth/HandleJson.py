# coding=utf-8
from utils.First.HandleTime import HandleTime
import utils.Fourth.ReadFromES as ReadFromES


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
        charge_times_eachday = 0
        car_num = dict()
        for i in data:
            if i.charge_times_eachday != '-32000.0' and i.charge_times_eachday != '-32000':
                charge_times_eachday += float(i.charge_times_eachday)
            if car_num.has_key(i.VNO):
                car_num[i.VNO] += 1
            else:
                car_num[i.VNO] = 0
        if car_num.__len__() == 0:
            jj['averChargeNum'] = 0
        else:
            jj['averChargeNum'] = charge_times_eachday / car_num.__len__()
        jj['totalChargeNum']=charge_times_eachday
        return jj