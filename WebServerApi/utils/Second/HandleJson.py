# coding=utf-8
import utils.Second.ReadFromES as ReadFromES
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
        peakChargeLength, valleyChargeLength, flatChargeLength = 0, 0, 0
        count1, count2, count3 = 0, 0, 0
        for i in data:
            if i.charge_time_peack != '-32000.0' and i.charge_time_peack != '-32000':
                peakChargeLength += i.charge_time_peack
                count1 += 1
            if i.charge_time_valley != '-32000.0' and i.charge_time_valley != '-32000':
                valleyChargeLength += i.charge_time_valley
                count2 += 1
            if i.charge_time_peace != '-32000.0' and i.charge_time_peace != '-32000':
                flatChargeLength += i.charge_time_peace
                count3 += 1
        if count1 == 0:
            jj['peakChargeLength'] = 0
        else:
            jj['peakChargeLength'] = peakChargeLength / count1
        if count2 == 0:
            jj['valleyChargeLength'] = 0
        else:
            jj['valleyChargeLength'] = valleyChargeLength / count2
        if count3 == 0:
            jj['flatChargeLength'] = 0
        else:
            jj['flatChargeLength'] = flatChargeLength / count3

        return jj
