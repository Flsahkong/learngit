#!/usr/bin/env python
# coding:utf-8

import tornado.httpserver
import tornado.options
import tornado.web
import tornado.ioloop
from ProvinceList import ProvinceList
from tornado.options import define, options

import utils.First.HandleJson as First
import utils.Second.HandleJson as Second
import utils.Third.HandleJson as Third
import utils.Fourth.HandleJson as Fourth
import utils.Fifth.HandleJson as Fifth
import utils.Sixth.HandleJson as Sixth
import utils.Seventh.HandleJson as Seventh
import utils.Eighth.HandleJson as Eight
import utils.Ninth.HandleJson as Ninth
import utils.Tenth.HandleJson as Tenth
import utils.Eleventh.HandleJson as Eleventh
import utils.Twelfth.HandleJson as Twelfth
import utils.Thirteenth.HandleJson as Thirteenth
import utils.Fourteenth.HandleJson as Fourteenth

define("port", default=8888, help="run on the given port", type=int)


class first(tornado.web.RequestHandler):
    def get(self):
        province = self.get_argument('province')
        startMonth = self.get_argument('startMonth')
        endMonth = self.get_argument('endMonth')
        try:
            province = province.encode('utf-8')
            startMonth = startMonth.encode('utf-8')
            endMonth = endMonth.encode('utf-8')
        except:
            pass
        province = provincelist.CodeToProDaiHao(province)
        if province == 'error':
            js = {"status": 1, "msg": "ERROR", "data": []}
            self.write(js)
        else:
            data, isTrue = First.Handler(province, startMonth, endMonth).getDataFromServer()
            if isTrue:
                js = {"status": 0, "msg": "SUCCESS", "data": data}
                self.write(js)
            else:
                js = {"status": 1, "msg": "ERROR", "data": data}
                self.write(js)


class second(tornado.web.RequestHandler):
    def get(self):
        province = self.get_argument('province')
        startMonth = self.get_argument('startMonth')
        endMonth = self.get_argument('endMonth')
        try:
            province = province.encode('utf-8')
            startMonth = startMonth.encode('utf-8')
            endMonth = endMonth.encode('utf-8')
        except:
            pass
        province = provincelist.CodeToProDaiHao(province)
        if province == 'error':
            js = {"status": 1, "msg": "ERROR", "data": []}
            self.write(js)
        else:
            data, isTrue = Second.Handler(province, startMonth, endMonth).getDataFromServer()
            if isTrue:
                js = {"status": 0, "msg": "SUCCESS", "data": data}
                self.write(js)
            else:
                js = {"status": 1, "msg": "ERROR", "data": data}
                self.write(js)


class third(tornado.web.RequestHandler):
    def get(self):
        province = self.get_argument('province')
        startMonth = self.get_argument('startMonth')
        endMonth = self.get_argument('endMonth')
        try:
            province = province.encode('utf-8')
            startMonth = startMonth.encode('utf-8')
            endMonth = endMonth.encode('utf-8')
        except:
            pass
        province = provincelist.CodeToProDaiHao(province)
        if province == 'error':
            js = {"status": 1, "msg": "ERROR", "data": []}
            self.write(js)
        else:
            data, isTrue = Third.Handler(province, startMonth, endMonth).getDataFromServer()
            if isTrue:
                js = {"status": 0, "msg": "SUCCESS", "data": data}
                self.write(js)
            else:
                js = {"status": 1, "msg": "ERROR", "data": data}
                self.write(js)


class fourth(tornado.web.RequestHandler):
    def get(self):
        province = self.get_argument('province')
        vehicleType = self.get_argument('vehicleType')
        startMonth = self.get_argument('startMonth')
        endMonth = self.get_argument('endMonth')
        try:
            province = province.encode('utf-8')
            startMonth = startMonth.encode('utf-8')
            endMonth = endMonth.encode('utf-8')
            vehicleType = vehicleType.encode('utf-8')
        except:
            pass
        province = provincelist.CodeToProDaiHao(province)
        if province == 'error':
            js = {"status": 1, "msg": "ERROR", "data": []}
            self.write(js)
        else:
            data, isTrue = Fourth.Handler(province, startMonth, endMonth).getDataFromServer()
            if isTrue:
                js = {"status": 0, "msg": "SUCCESS", "data": data}
                self.write(js)
            else:
                js = {"status": 1, "msg": "ERROR", "data": data}
                self.write(js)


class fifth(tornado.web.RequestHandler):
    def get(self):
        province = self.get_argument('province')
        vehicleType = self.get_argument('vehicleType')  # 由于vehicleType在表中没有体现，所以直接取所有的车辆类型,vehicleType不在起作用
        startMonth = self.get_argument('startMonth')
        endMonth = self.get_argument('endMonth')
        try:
            province = province.encode('utf-8')
            startMonth = startMonth.encode('utf-8')
            endMonth = endMonth.encode('utf-8')
        except:
            pass
        province = provincelist.CodeToProDaiHao(province)
        if province == 'error':
            js = {"status": 1, "msg": "ERROR", "data": []}
            self.write(js)
        else:
            data, isTrue = Fifth.Handler(province, startMonth, endMonth).getDataFromServer()
            if isTrue:
                js = {"status": 0, "msg": "SUCCESS", "data": data}
                self.write(js)
            else:
                js = {"status": 1, "msg": "ERROR", "data": data}
                self.write(js)


class sixth(tornado.web.RequestHandler):
    def get(self):
        VNO = self.get_argument("VNO")
        dueDate = self.get_argument("dueDate")
        try:
            VNO = VNO.encode('utf-8')
            dueDate = dueDate.encode('utf-8')
        except:
            pass
        data, isTrue = Sixth.Handler(VNO, dueDate).getDataFromServer()
        if isTrue:
            js = {"status": 0, "msg": "SUCCESS", "data": data}
            self.write(js)
        else:
            js = {"status": 1, "msg": "ERROR", "data": data}
            self.write(js)


class seventh(tornado.web.RequestHandler):
    def get(self):
        province = self.get_argument('province')
        startMonth = self.get_argument('startMonth')
        endMonth = self.get_argument('endMonth')
        try:
            province = province.encode('utf-8')
            startMonth = startMonth.encode('utf-8')
            endMonth = endMonth.encode('utf-8')
        except:
            pass
        province = provincelist.CodeToProDaiHao(province)
        if province == 'error':
            js = {"status": 1, "msg": "ERROR", "data": []}
            self.write(js)
        else:
            data, isTrue = Seventh.Handler(province, startMonth, endMonth).getDataFromServer()
            if isTrue:
                js = {"status": 0, "msg": "SUCCESS", "data": data}
                self.write(js)
            else:
                js = {"status": 1, "msg": "ERROR", "data": data}
                self.write(js)


class eighth(tornado.web.RequestHandler):
    def get(self):
        VNO = self.get_argument("VNO")
        startMonth = self.get_argument("startMonth")
        endMonth = self.get_argument("endMonth")
        try:
            VNO = VNO.encode('utf-8')
            startMonth = startMonth.encode('utf-8')
            endMonth = endMonth.encode('utf-8')
        except:
            pass
        data, isTrue = Eight.Handler(VNO, startMonth, endMonth).getDataFromServer()
        if isTrue:
            js = {"status": 0, "msg": "SUCCESS", "data": data}
            self.write(js)
        else:
            js = {"status": 1, "msg": "ERROR", "data": data}
            self.write(js)


class ninth(tornado.web.RequestHandler):
    def get(self):
        province = self.get_argument('province')
        startMonth = self.get_argument('startMonth')
        endMonth = self.get_argument('endMonth')
        try:
            province = province.encode('utf-8')
            startMonth = startMonth.encode('utf-8')
            endMonth = endMonth.encode('utf-8')
        except:
            pass
        province = provincelist.CodeToProDaiHao(province)
        if province == 'error':
            js = {"status": 1, "msg": "ERROR", "data": []}
            self.write(js)
        else:
            data, isTrue = Ninth.Handler(province, startMonth, endMonth).getDataFromServer()
            if isTrue:
                js = {"status": 0, "msg": "SUCCESS", "data": data}
                self.write(js)
            else:
                js = {"status": 1, "msg": "ERROR", "data": data}
                self.write(js)


class tenth(tornado.web.RequestHandler):
    def get(self):
        VNO = self.get_argument("vno")
        startMonth = self.get_argument("startMonth")
        endMonth = self.get_argument("endMonth")
        try:
            VNO = VNO.encode('utf-8')
            startMonth = startMonth.encode('utf-8')
            endMonth = endMonth.encode('utf-8')
        except:
            pass
        data, isTrue = Tenth.Handler(VNO, startMonth, endMonth).getDataFromServer()
        if isTrue:
            js = {"status": 0, "msg": "SUCCESS", "data": data}
            self.write(js)
        else:
            js = {"status": 1, "msg": "ERROR", "data": data}
            self.write(js)


class eleventh(tornado.web.RequestHandler):
    def get(self):
        province = self.get_argument('province')
        startMonth = self.get_argument('startMonth')
        endMonth = self.get_argument('endMonth')
        range = self.get_argument("range")
        try:
            province = province.encode('utf-8')
            startMonth = startMonth.encode('utf-8')
            endMonth = endMonth.encode('utf-8')
            range = range.encode('utf-8')
        except:
            pass
        province = provincelist.CodeToProDaiHao(province)
        if province == 'error':
            js = {"status": 1, "msg": "ERROR", "data": []}
            self.write(js)
        else:
            data, isTrue = Eleventh.Handler(province, startMonth, endMonth, range).getDataFromServer()
            if isTrue:
                js = {"status": 0, "msg": "SUCCESS", "data": data}
                self.write(js)
            else:
                js = {"status": 1, "msg": "ERROR", "data": data}
                self.write(js)


class twelfth(tornado.web.RequestHandler):
    def get(self):
        province = self.get_argument('province')
        startMonth = self.get_argument('startMonth')
        endMonth = self.get_argument('endMonth')
        range = self.get_argument("range")
        try:
            province = province.encode('utf-8')
            startMonth = startMonth.encode('utf-8')
            endMonth = endMonth.encode('utf-8')
            range = range.encode('utf-8')
        except:
            pass
        province = provincelist.CodeToProDaiHao(province)
        if province == 'error':
            js = {"status": 1, "msg": "ERROR", "data": []}
            self.write(js)
        else:
            data, isTrue = Twelfth.Handler(province, startMonth, endMonth, range).getDataFromServer()
            if isTrue:
                js = {"status": 0, "msg": "SUCCESS", "data": data}
                self.write(js)
            else:
                js = {"status": 1, "msg": "ERROR", "data": data}
                self.write(js)


class thirteenth(tornado.web.RequestHandler):

    def get(self):
        province = self.get_argument('province')
        startMonth = self.get_argument('startMonth')
        endMonth = self.get_argument('endMonth')
        vehicletype = self.get_argument('vehicletype', 'all')
        try:
            province = province.encode('utf-8')
            startMonth = startMonth.encode('utf-8')
            endMonth = endMonth.encode('utf-8')
            vehicletype = vehicletype.encode('utf-8')
        except:
            pass
        province = provincelist.CodeToProvince(province)
        if province == 'error':
            js = {"status": 1, "msg": "ERROR", "data": []}
            self.write(js)
        else:
            data, isTrue = Thirteenth.Handler(province, startMonth, endMonth, vehicletype).getDataFromServer()
            if isTrue:
                js = {"status": 0, "msg": "SUCCESS", "data": data}
                self.write(js)
            else:
                js = {"status": 1, "msg": "ERROR", "data": data}
                self.write(js)


class fourteenth(tornado.web.RequestHandler):
    def get(self):
        province = self.get_argument('province')
        startMonth = self.get_argument('startMonth')
        endMonth = self.get_argument('endMonth')
        vehicletype = self.get_argument('vehicletype', 'all')
        try:
            province = province.encode('utf-8')
            startMonth = startMonth.encode('utf-8')
            endMonth = endMonth.encode('utf-8')
            vehicletype = vehicletype.encode('utf-8')
        except:
            pass
        province = provincelist.CodeToProvince(province)
        if province == 'error':
            js = {"status": 1, "msg": "ERROR", "data": []}
            self.write(js)
        else:
            data, isTrue = Fourteenth.Handler(province, startMonth, endMonth, vehicletype).getDataFromServer()
            if isTrue:
                js = {"status": 0, "msg": "SUCCESS", "data": data}
                self.write(js)
            else:
                js = {"status": 1, "msg": "ERROR", "data": data}
                self.write(js)


if __name__ == "__main__":
    provincelist = ProvinceList()
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[
        (r"/cdfs", first),
        (r"/cdsd", second),
        (r"/cdsc", third),
        (r"/yjcdcs", fourth),
        (r"/cdl", fifth),
        (r"/zxslc", sixth),
        (r"/yzxslc", seventh),      #第七个得到的list很大，运行时间可能比较长
        (r"/yjjcs", eighth),
        (r"/yjjscs", ninth),
        (r"/bglnh", tenth),
        (r"/cdqssoc", eleventh),
        (r"/cdjssoc", twelfth),
        (r"/dcjkd", thirteenth),
        (r"/dcjkdcltj", fourteenth)
    ])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
