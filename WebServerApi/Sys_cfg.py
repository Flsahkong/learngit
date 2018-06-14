# -*- coding: utf-8 -*-
import ConfigParser

class addr:
    db_host = ""
    db_port = ""

    @classmethod
    def addr_read_fun(cls):
        cf = ConfigParser.ConfigParser()
        cf.read("Sys_Addr_cfg.ini")
        cls.db_host = cf.get("sysaddrcfg", "host")
        cls.db_port = cf.getint("sysaddrcfg", "port")
