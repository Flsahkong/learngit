# coding=utf-8
import utils.Seventh.ReadFromES as ReadFromES
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
        jj["month"] = self.handle.reversehandle(time[1])
        energy_all, mile_per_kWh = 0, 0
        total_mail = 0
        car_num = dict()
        for i in data:
            if i.energy_all != '-32000.0' and i.energy_all != '-32000' and i.mile_per_kWh != '-32000' and \
                    i.mile_per_kWh != '-32000.0':
                total_mail += float(i.energy_all) * float(i.mile_per_kWh)
            if car_num.has_key(i.VNO):
                car_num[i.VNO] += 1
            else:
                car_num[i.VNO] = 0

        jj['totalMile']=total_mail
        if car_num.__len__()==0:
            jj['averMile']=0
        else:
            jj['averMile']=total_mail/car_num.__len__()
        return jj
