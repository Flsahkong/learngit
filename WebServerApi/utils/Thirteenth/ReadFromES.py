# coding=utf-8
from thrift import Thrift
from thrift.transport import TSocket
from thrift.protocol import TMultiplexedProtocol
from ESmodel.ttypes import *
from ESTypeEnum.ttypes import *
from ESService import SearchData
import Sys_cfg as addrcfg

class battery_original_data(object):
    def __init__(self, time="", B2="", B3="", B4=""):
        self.BatteryHealth_HealthScore = time
        self.BatteryHealth_ScoreAh = B2
        self.BatteryHealth_ScoreConsistency = B3
        self.BatteryHealth_Time = B4


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

    def get_battery_data(self, province, startmonth, endmonth, vehicletype):  # 获取电池数据
        Vehiclelist = []

        if not self.constate:
            return Vehiclelist
        try:
            if province == '全国':
                query_string = "A_source:BatteryHealth_Table AND BatteryHealth_Time:[%s TO %s] " % (
                    startmonth, endmonth)
            else:
                query_string = "A_source:BatteryHealth_Table AND BatteryHealth_Province:%s AND BatteryHealth_Time: " \
                               "[%s TO %s] " % (province, startmonth, endmonth)
            if vehicletype == "all":
                queryString = query_string + " | report count(A_source) on " \
                                             "BatteryHealth_HealthScore," \
                                             "BatteryHealth_ScoreAh," \
                                             "BatteryHealth_ScoreConsistency"
            else:
                queryString = query_string + " AND BatteryHealth_VehicleType:%s | report " \
                                             "count(A_source) on BatteryHealth_HealthScore," \
                                             "BatteryHealth_ScoreAh," \
                                             "BatteryHealth_ScoreConsistency" % vehicletype

            query_model = TQueryModel(a_from=0, a_to=0, queryString=queryString)
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
    a, bo = conn.get_battery_data('全国', '2016-01-01', '2018-03-01', 'all')
