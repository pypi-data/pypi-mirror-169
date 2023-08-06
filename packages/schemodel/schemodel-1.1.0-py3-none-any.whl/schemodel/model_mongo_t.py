#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: CC
# @Time  : 2022/9/30 15:35
from pymongo import MongoClient
from schemv.types import StringType, IntType

from schemodel.schemodel.base_item import BaseItem

mongo_client = MongoClient("", connect=False)


class SearchItemBase(BaseItem):
    DATABASE = 'spider_db'
    TABLE = 'test'
    DB_TYPE = 'mongodb'
    session = mongo_client[DATABASE][TABLE]


class SearchItem(SearchItemBase):
    name = StringType(required=True)
    age = IntType(required=True)


if __name__ == '__main__':
    base_item = SearchItem()
    base_item.name = "123"
    base_item.age = 20
    base_item.save()
