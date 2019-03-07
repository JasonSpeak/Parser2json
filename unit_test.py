#!/usr/bin/python
# -*- coding: utf-8 -*-

import parser2json

'''test for dat2json'''
keyList = ["1","2","3"]
parser2json.dat2json("test_dat2json.dat",keyList,",")

'''test for xml_config2json'''
#parser2json.xml_config2json('test_config.config')


'''test for ini2json'''
#parser2json.ini2json('client.ini')