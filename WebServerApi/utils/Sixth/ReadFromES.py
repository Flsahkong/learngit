# coding=utf-8
from thrift import Thrift
from thrift.transport import TSocket
from thrift.protocol import TMultiplexedProtocol
from ESmodel.ttypes import *
from ESTypeEnum.ttypes import *
from ESService import SearchData


class battery_original_data(object):
    def __init__(self, time=""):
        self.mile_all = time


class CarVnoClass(object):
    def __init__(self, vno):
        self.vno = vno


class scan_data_fun(object):
    __instance = None

    def __init__(self):
        self.constate = False
        self.client = None
        self.connectEserv()

    def connectEserv(self):
        try:
            self.tsocket = TSocket.TSocket('10.0.1.145', 6060)
            self.transport = TTransport.TFramedTransport(self.tsocket)

            # Wrap in a protocol
            self.protocol = TBinaryProtocol.TBinaryProtocol(self.transport)
            self.service = TMultiplexedProtocol.TMultiplexedProtocol(self.protocol,
                                                                     "com.aleiye.client.service.search.SearchData")

            self.client = SearchData.Client(self.service)
            self.transport.open()
            self.constate = True

        except Thrift.TException as tx:
            self.constate = False
            pass

    def __del__(self):
        if self.constate:
            self.transport.close()

    def get_battery_data(self, VNO, starttime):  # 获取电池数据
        Vehiclelist = []
        endtime = starttime[0:9] + str(int(starttime[-1])+1)
        if not self.constate:
            return Vehiclelist
        try:
            query_string = "A_source:vehicle_all_drive_table AND time_end : [%s TO %s] AND VNO: %s  | report count(" \
                           "A_source) on mile_all" % (
                                                                                starttime, endtime, VNO)
            query_model = TQueryModel(a_from=0, a_to=0,
                                      queryString=query_string)  # AND B10:>2 AND B5:>0 AND  B4:<-2.0 AND G7:<1.0
            result = self.client.queryReport(query_model)
            Vehiclelist = result.datas
        except Thrift.TException as tx:
            print tx.message
            return Vehiclelist, False
        except Exception, e:
            print e.message
            return Vehiclelist, False
        return Vehiclelist, True


if __name__ == "__main__":
    conn = scan_data_fun()
    a, bo = conn.get_battery_data('鲁AC1Y37', "2018-02-05")
    for i in a:
        print(i.mile_all)
