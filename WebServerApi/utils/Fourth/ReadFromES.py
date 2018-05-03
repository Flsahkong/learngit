# coding=utf-8
from thrift import Thrift
from thrift.transport import TSocket
from thrift.protocol import TMultiplexedProtocol
from ESmodel.ttypes import *
from ESTypeEnum.ttypes import *
from ESService import SearchData


class battery_original_data(object):
    def __init__(self, time="", B=""):
        self.charge_times_eachday = time
        self.VNO = B


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

    def get_battery_data(self, province, startTime, endTime):  # 获取电池数据
        Vehiclelist = []

        if not self.constate:
            return Vehiclelist
        try:
            if province == '全国':
                query_string = "A_source:vehicle_all_charge_table AND Time : [%s TO %s]  | report count(A_source) on " \
                               "VNO,charge_times_eachday" % (startTime, endTime)
            else:
                query_string = "A_source:vehicle_all_charge_table AND Time : [%s TO %s] AND T_vehicle_region:%s  | " \
                               "report count(A_source) on VNO,charge_times_eachday" % (
                    startTime, endTime, province)
            query_model = TQueryModel(a_from=0, a_to=0,
                                      queryString=query_string)
            result = self.client.queryReport(query_model)  # 总数据
            Vehiclelist=result.datas

        except Thrift.TException as tx:
            print tx.message
            return Vehiclelist, False
        except Exception, e:
            print e.message
            return Vehiclelist, False
        return Vehiclelist, True


if __name__ == "__main__":
    conn = scan_data_fun()
    a, bo = conn.get_battery_data('全国', '2017-01-01', '2017-02-01')
    for i in a:
        print(i.charge_times_eachday, i.VNO)
