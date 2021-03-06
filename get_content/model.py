# __author__ = 'fit'
# -*- coding: utf-8 -*-
from peewee import *

db = MySQLDatabase(database="pachong", host="192.168.0.114", port=3306, user="root", passwd="fit123456",
                   charset="utf8")
db.connect()


# 龙虎榜orm模型定义
class longhubang(Model):
    stock_code = CharField()
    date = DateField()
    department = CharField()
    buy = DoubleField(null=True)
    buy_percent = DoubleField(null=True)
    sell = DoubleField(null=True)
    sell_percent = DoubleField(null=True)
    net = DoubleField(null=True)
    reason = CharField(null=True)
    tag = IntegerField()
    serial_number = IntegerField(null=True)

    class Meta:
        database = db
