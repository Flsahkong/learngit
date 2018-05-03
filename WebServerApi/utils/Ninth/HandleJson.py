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
        jj["month"] = self.handle.reversehandle(time[0])
        car_drive_times = 0
        car_num = dict()
        for i in data:
            if i[1] != '-32000.0' and i[1] != '-32000':
                car_drive_times += float(i[1]) * int(i[2])
                # 跟上一个接口一样，仅当有数据的时候才进行统计这辆车
                if car_num.has_key(i[0]):
                    car_num[i[0]] += 1
                else:
                    car_num[i[0]] = 0
        if car_num.__len__() == 0:
            jj['value'] = 0
        else:
            jj['value'] = car_drive_times / car_num.__len__()
        return jj
