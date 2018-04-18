# coding=utf-8
import utils.Ninth.ReadFromES as ReadFromES
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
        car_drive_times = 0
        car_num = dict()
        for i in data:
            if i.drive_times_eachday != '-32000.0' and i.drive_times_eachday != '-32000':
                car_drive_times += float(i.drive_times_eachday)
            if car_num.has_key(i.VNO):
                car_num[i.VNO] += 1
            else:
                car_num[i.VNO] = 0
        if car_num.__len__()==0:
            jj['value']=0
        else:
            jj['value']=car_drive_times/car_num.__len__()
        return jj