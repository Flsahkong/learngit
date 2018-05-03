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
        normal, high, low = 0, 0, 0
        if data.__len__() == 3:
            if data[0][0] == "-32000" or data[0][0] == "-32000.0":
                normal = int(data[0][1])
                if data[1][0] == "快充":
                    high = int(data[1][1])
                    low = int(data[2][1])
                else:
                    low = int(data[1][1])
                    high = int(data[2][1])
                jj['fastChargeNum'] = int(normal / 2) + high
                jj['slowChargeNum'] = normal - int(normal / 2) + low
            elif data[0][0] == "快充":
                high = int(data[0][1])
                if data[1][0] == "-32000" or data[1][0] == "-32000.0":
                    normal = int(data[1][1])
                    low = int(data[2][1])
                else:
                    low = int(data[1][1])
                    normal = int(data[2][1])
                jj['fastChargeNum'] = int(normal / 2) + high
                jj['slowChargeNum'] = normal - int(normal / 2) + low
            elif data[0][0] == "慢充":
                low = int(data[0][1])
                if data[1][0] == "-32000" or data[1][0] == "-32000.0":
                    normal = int(data[1][1])
                    high = int(data[2][1])
                else:
                    high = int(data[1][1])
                    normal = int(data[2][1])
                jj['fastChargeNum'] = int(normal / 2) + high
                jj['slowChargeNum'] = normal - int(normal / 2) + low
        elif data.__len__() == 2:
            if data[0][0] == "-32000" or data[0][0] == "-32000.0":
                normal = int(data[0][0])
                if data[1][0] == "快充":
                    high = int(data[1][1])
                else:
                    low = int(data[1][1])
                jj['fastChargeNum'] = int(normal / 2) + high
                jj['slowChargeNum'] = normal - int(normal / 2) + low
            elif data[0][0] == "快充":
                high = int(data[0][1])
                if data[1][0] == "-32000" or data[1][0] == "-32000.0":
                    normal = int(data[1][1])
                else:
                    low = int(data[1][1])
                jj['fastChargeNum'] = int(normal / 2) + high
                jj['slowChargeNum'] = normal - int(normal / 2) + low
            elif data[0][0] == "慢充":
                low = int(data[0][1])
                if data[1][0] == "-32000" or data[1][0] == "-32000.0":
                    normal = int(data[1][1])
                else:
                    high = int(data[1][1])
                jj['fastChargeNum'] = int(normal / 2) + high
                jj['slowChargeNum'] = normal - int(normal / 2) + low
        elif data.__len__() == 1:
            if data[0][0] == "-32000" or data[0][0] == "-32000.0":
                normal = int(data[0][1])
            elif data[0][0] == "快充":
                high = int(data[0][1])
            elif data[0][0] == "慢充":
                low = int(data[0][1])
            jj['fastChargeNum'] = int(normal / 2) + high
            jj['slowChargeNum'] = normal - int(normal / 2) + low
        else:
            jj['fastChargeNum'] = 0
            jj['slowChargeNum'] = 0
        return jj
