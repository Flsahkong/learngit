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
        peakChargeLength, valleyChargeLength, flatChargeLength = 0.0, 0.0, 0.0
        # count1, count2, count3 = 0, 0, 0
        for i in data:
            if i[0] != '-32000.0' and i[0] != '-32000':
                peakChargeLength += float(i[0])*float(i[3])
                # count1 += int(i[3])
            if i[1] != '-32000.0' and i[1] != '-32000':
                valleyChargeLength += float(i[1])*float(i[3])
                # count2 += int(i[3])
            if i[2] != '-32000.0' and i[2] != '-32000':
                flatChargeLength += float(i[2])*float(i[3])
                # count3 += int(i[3])
        # if count1 == 0:
        #     jj['peakChargeLength'] = 0
        # else:
        #     jj['peakChargeLength'] = peakChargeLength / count1
        # if count2 == 0:
        #     jj['valleyChargeLength'] = 0
        # else:
        #     jj['valleyChargeLength'] = valleyChargeLength / count2
        # if count3 == 0:
        #     jj['flatChargeLength'] = 0
        # else:
        #     jj['flatChargeLength'] = flatChargeLength / count3
        jj['peakChargeLength'] = peakChargeLength
        jj['valleyChargeLength'] = valleyChargeLength
        jj['flatChargeLength'] = flatChargeLength
        return jj
