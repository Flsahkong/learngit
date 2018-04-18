import utils.Tenth.ReadFromES as ReadFromES
from utils.First.HandleTime import HandleTime


class Handler:
    def __init__(self, VNO, startMonth, endMonth):
        self.VNO = VNO
        self.startMonth = startMonth
        self.endMonth = endMonth

    def getDataFromServer(self):
        connect = ReadFromES.scan_data_fun()
        self.handle = HandleTime(self.startMonth, self.endMonth)
        self.time = self.handle.handle()

        List = []
        for i in self.time:
            Data, isTrue = connect.get_battery_data(self.VNO, i[0], i[1])
            if isTrue == False:
                return [], False
            List.append(self.computeResult(Data, i))
        return List, True

    def computeResult(self, data, time):
        jj = dict()
        jj["month"] = self.handle.reversehandle(time[1])
        times = 0
        count = 0
        for i in data:
            if i.energy_aver_100 == "-32000" or i.energy_aver_100 == "-32000.0":
                pass
            else:
                time += float(i.drive_times_eachday)
                count += 1
        if count == 0:
            jj["value"] = 0
        else:
            jj["value"] = times / count

        return jj
