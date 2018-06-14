# coding=utf-8
from thrift import Thrift
from thrift.transport import TSocket
from thrift.protocol import TMultiplexedProtocol
from ESmodel.ttypes import *
from ESTypeEnum.ttypes import *
from ESService import SearchData
import Sys_cfg as addrcfg

class battery_original_data(object):
    def __init__(self, time=""):
        self.drive_times_eachday= time


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
            self.tsocket = TSocket.TSocket(addrcfg.addr.db_host, addrcfg.addr.db_port)
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

    def get_battery_data(self, VNO, starttime,endtime):  # 获取电池数据
        Vehiclelist = []

        if not self.constate:
            return Vehiclelist
        try:
            query_string = "A_source:vehicle_all_drive_table AND time_end : [%s TO %s] AND VNO: %s | report count(" \
                           "A_source) on drive_times_eachday" % (starttime, endtime, VNO)
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
    addr = addrcfg.addr()
    addr.addr_read_fun()
    conn = scan_data_fun()
    a, bo = conn.get_battery_data('鲁AC1Y37', "2018-02-01", "2018-02-28")
    for i in a:
        print(i.drive_times_eachday)
