import utils.Thirteenth.ReadFromES as ReadFromES
from utils.Thirteenth.HandleTime import HandleTime

class Handler:
    def __init__(self, province, startMonth, endMonth, vehicletype):
        self.province = province
        self.startMonth = startMonth
        self.endMonth = endMonth
        self.vehicletype = vehicletype

    def getDataFromServer(self):
        connect = ReadFromES.scan_data_fun()
        self.handle = HandleTime(self.startMonth, self.endMonth)
        self.time = self.handle.hanle()

        Data,isTrue = connect.get_battery_data(self.province, self.vehicletype)
        if isTrue == False:
            return [], False
        else:
            return self.computeResult(Data),True


    def computeResult(self, Data):
        BatteryHealth_HealthScore, BatteryHealth_NowAh, BatteryHealth_ScoreConsistency = 0, 0, 0
        size = Data.__len__()
        if size != 0:
            List = []
            count = []
            for i in self.time:
                jj = dict()
                jj["month"] = self.handle.reversehandle(i)
                jj["healthScore"] = 0
                jj["capacityScore"] = 0
                jj["consistencyScore"] = 0
                List.append(jj)
                count.append(0)

            for m in Data:
                try:
                    index = self.time.index(m.BatteryHealth_Time)
                    List[index]["healthScore"] += float(m.BatteryHealth_HealthScore)
                    List[index]["capacityScore"] += float(m.BatteryHealth_ScoreAh)
                    List[index]["consistencyScore"] += float(m.BatteryHealth_ScoreConsistency)
                    count[index] += 1
                except ValueError:
                    pass

            for i in range(len(self.time)):
                try:
                    List[i]["healthScore"] /=count[i]
                    List[i]["capacityScore"] /= count[i]
                    List[i]["consistencyScore"] /= count[i]
                except ZeroDivisionError:
                    pass

            return List
        else:
            List = []
            for num in self.time:
                jj = dict()
                jj["month"] = self.handle.reversehandle(num)
                jj["healthScore"] = 0
                jj["capacityScore"] = 0
                jj["consistencyScore"] = 0
                List.append(jj)
            return List
