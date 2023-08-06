#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: CC
# @Time  : 2022/9/30 14:19

import curd
from pymongo import collection
from schemv import Model


class BaseItem(Model):
    # 数据库名称
    DATABASE = None
    # 表名称
    TABLE = None
    # 数据库类型(mysql, mongodb)
    DB_TYPE = 'mysql'
    # 执行增删改查数据库对象
    session: [curd.Session, collection.Collection] = None

    def __init__(self, raw_data=None, trusted_data=None, deserialize_mapping=None,
                 init=True, partial=True, strict=True, validate=False, app_data=None,
                 lazy=False, **kwargs):
        super(BaseItem, self).__init__(raw_data, trusted_data, deserialize_mapping,
                                       init, partial, strict, validate, app_data,
                                       lazy, **kwargs)
        assert self.DATABASE is not None, "DATABASE cannot be None"
        assert self.TABLE is not None, "TABLE cannot be None"
        assert self.session is not None, "session cannot be None"
        if self.DB_TYPE == 'mongodb':
            assert isinstance(self.session, collection.Collection), '必须为mongodb Collection 对象'
        else:
            assert isinstance(self.session, curd.Session), '必须为curd.session 对象'

    def save(self):
        self.validate()
        data = self.to_primitive()
        if self.DB_TYPE == 'mongodb':
            self.session.insert_one(data)
        else:
            self.session.create(f"{self.DATABASE}.{self.TABLE}", data)
