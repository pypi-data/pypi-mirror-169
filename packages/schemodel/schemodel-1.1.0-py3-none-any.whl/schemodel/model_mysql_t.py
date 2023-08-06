#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: CC
# @Time  : 2022/9/30 15:35
from schemv.types import StringType, IntType

from schemodel.schemodel.base_item import BaseItem


def get_curd_session():
    return object


class SearchItemBase(BaseItem):
    DATABASE = 'spider_db'
    TABLE = 'test'
    DB_TYPE = 'mysql'
    session = get_curd_session()


class SearchItem(SearchItemBase):
    name = StringType(required=True)
    age = IntType(required=True)


if __name__ == '__main__':
    base_item = SearchItem()
    base_item.name = "123"
    base_item.age = 30
    base_item.save()
