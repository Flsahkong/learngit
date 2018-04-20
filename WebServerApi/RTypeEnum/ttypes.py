#
# Autogenerated by Thrift Compiler (0.9.2)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class RFieldTypeEnum:
  STRING = 0
  SHORT = 1
  INTEGER = 2
  LONG = 3
  FLOAT = 4
  DOUBLE = 5
  BINARY = 6
  BYTE = 7
  BOOLEAN = 8
  TIMESTAMP = 9
  DATE = 10
  DECIMAL = 11

  _VALUES_TO_NAMES = {
    0: "STRING",
    1: "SHORT",
    2: "INTEGER",
    3: "LONG",
    4: "FLOAT",
    5: "DOUBLE",
    6: "BINARY",
    7: "BYTE",
    8: "BOOLEAN",
    9: "TIMESTAMP",
    10: "DATE",
    11: "DECIMAL",
  }

  _NAMES_TO_VALUES = {
    "STRING": 0,
    "SHORT": 1,
    "INTEGER": 2,
    "LONG": 3,
    "FLOAT": 4,
    "DOUBLE": 5,
    "BINARY": 6,
    "BYTE": 7,
    "BOOLEAN": 8,
    "TIMESTAMP": 9,
    "DATE": 10,
    "DECIMAL": 11,
  }
