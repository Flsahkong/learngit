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
        jj["VNO"] = self.VNO
        total = 0
        num = 0
        for i in data:
            if i[0] != "-32000" and i[0] != "-32000.0":
                a = int(i[1])
                total += float(i[0]) * a
                num += a
        if num == 0:
            jj["totalMile"] = 0
        else:
            jj["totalMile"] = total / num

        return jj
