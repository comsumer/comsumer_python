#! /usr/bin/env python
#coding = utf-8

from collections import OrderedDict

from pyexcel_xls import get_data
from pyexcel_xls import save_data

def read_xls_file():
    xls_data = get_data(r"investorlist20170720.xlsx")