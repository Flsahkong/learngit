import utils.Thirteenth.ReadFromES as ReadFromES
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

        # Data,isTrue = connect.get_battery_data(self.province, self.vehicletype)
        # if isTrue == False:
        #     return [], False
        # else:
        #     return self.computeResult(Data),True

        List = []
        for i in self.time:
            Data, isTrue = connect.get_battery_data(self.province, i[0], i[1], vehicletype=self.vehicletype)
            if isTrue == False:
                return [], False
            List.append(self.computeResult(Data, i))
        return List, True

    def computeResult(self, Data, time):
        jj = dict()
        jj["month"] = self.handle.reversehandle(time[0])

        BatteryHealth_HealthScore, BatteryHealth_NowAh, BatteryHealth_ScoreConsistency = 0, 0, 0
        count1, count2, count3 = 0, 0, 0

        for i in Data:
            if i[0] != "-32000" and i[0] != "-32000.0":
                BatteryHealth_HealthScore += float(i[0]) * int(i[3])
                count1 += int(i[3])

            if i[1] != "-32000" and i[1] != "-32000.0":
                BatteryHealth_NowAh += float(i[1]) * int(i[3])
                count2 += int(i[3])

            if i[2] != "-32000" and i[2] != "-32000.0":
                BatteryHealth_ScoreConsistency += float(i[2]) * int(i[3])
                count3 += int(i[3])

        jj["healthScore"] = BatteryHealth_HealthScore / count1 if count1 != 0 else 0
        jj["capacityScore"] = BatteryHealth_NowAh / count2 if count2 != 0 else 0
        jj["consistencyScore"] = BatteryHealth_ScoreConsistency / count3 if count3 != 0 else 0

        return jj
