# coding=utf-8
import utils.Sixth.ReadFromES as ReadFromES


class Handler:
    def __init__(self, VNO, dueDate):
        self.VNO = VNO
        self.dueDate = dueDate

    def getDataFromServer(self):
        connect = ReadFromES.scan_data_fun()
        self.data = self.dueDate[0:4] + "-" + self.dueDate[4:6] + "-" + self.dueDate[6:]

        Data, isTrue = connect.get_battery_data(self.VNO, self.data)
        if isTrue == False:
            return [], False

        return self.computeResult(Data), True

    def computeResult(self, data):
        jj = dict()
        jj["dueDate"] = self.dueDate
        jj["VNO"]=self.VNO
        total = 0
        for i in data:
            if i.mile_all == "-32000" or i.mile_all == "-32000.0":
                a = 0
            else:
                a = float(i.mile_all)
            total += a
        if len(data) == 0:
            jj["totalMile"] = 0
        else:
            jj["totalMile"] = total / len(data)

        return jj
