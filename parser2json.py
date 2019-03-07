#!/usr/bin/python
# -*- coding: utf-8 -*-

# /*
#  * @Author: Jimi.shiqingwei 
#  * @Date: 2019-03-07 15:32:22 
#  * @Last Modified by:   Jimi.shiqingwei 
#  * @Last Modified time: 2019-03-07 15:32:22 
#  */

#TODO dat to json:√
#TODO xml to json:√
#TODO ini to json:√
#TODO yaml to json：√
#TODO config to json：√

import configparser
import json
import os
import sys

import xmltodict
import yaml


def dat2json(datFile_location,keyList,splitStr): 
    '''
    #Description:
      #Parser dat file to json file
      #dat file should be string value split with splitStr
      #users should input a dat file location,a keyList and a splitStr
      #this function will create config.json under the same folder
    #Args:
      #datFile(string): dat file's location
      #keyList(list): dat values' key
      #splitStr: split string in this datFile
    #Returns:
      #NULL
    #Raises:
      #OSError: A error occurred while open the dat file 
      #Unexpected error: read the error info
    '''
    json_data = []

    ##get dat data and transform to json data
    try:
      datFile = open(datFile_location,'r')
    except OSError as error:
      print ('Handling open dat file error:',error)
    except:
      print ("Unexpected error:", sys.exc_info()[0])  
      
    for line in datFile.readlines():
        line = line.strip()
        valueList = line.split(splitStr)
        json_str = '{'
        for i in range(len(valueList)):
            #TODO : how to solve location \ problem or such symbol
            json_str = json_str + '"' + keyList[i] + '":"' + valueList[i].replace("\\","\\\\") + '"'
            if i<len(valueList)-1:
                 json_str = json_str + ',' 
        json_str = json_str + '}'       
        print (json_str)
        json_node = json.loads(json_str)
        json_data.append(json_node)   
    datFile.close()

    ##creat a json file under the folder and write json data in 
    try:
      jsonFile = open("config.json","w")
    except OSError as error:
      print ('Handling create json file error:',error)
    except:
      print ("Unexpected error:", sys.exc_info()[0])
    else:
      json.dump(json_data,jsonFile)
      jsonFile.close()

        

def xml_config2json(xml_configFile_Location):
    '''
    #Description:
      #Parser xml or config file to json file
      #users should input a xml or config file's location
      #this function will create xml_config2json.json under the same folder
    #Args:
      #xml_configFile_Location: the location of the xml or config file to parse
    #Returns:
      #NULL
    #Raises:
      #OSError: A error occurred while open the xml or config file 
      #Unexpected error: read the error info
    ''' 
    ##get xml or config data and transform to json data
    ##this xml or config file must be opend with 'rb' mode
    try:
      xml_configFile = open(xml_configFile_Location,'rb')
    except OSError as error:
      print ('Handling open xml file error:',error)
    except:
      print ("Unexpected error:", sys.exc_info()[0]) 

    data = xmltodict.parse(xml_configFile)
    xml_configFile.close()

    ##creat a json file under the folder and write json data in 
    try:
      jsonFile = open("xml_config2json.json","w")
    except OSError as error:
      print ('Handling create json file error:',error)
    except:
      print ("Unexpected error:", sys.exc_info()[0])
    else:
      json.dump(data,jsonFile)
      jsonFile.close()


def ini2json(iniFile_Location):
    '''
    #Description:
      #Parser ini file to json file
      #users should input a ini file's location
      #this function will create ini2json.json under the same folder
    #Args:
      #iniFile_Location: the location of the ini file to parse
    #Returns:
      #NULL
    #Raises:
      #OSError: A error occurred while open the ini file 
      #Unexpected error: read the error info
    '''
    config = configparser.ConfigParser()
    try:
      config.read(iniFile_Location)
    except OSError as error:
      print ('Handling open ini file error:',error)
    except:
      print ("Unexpected error:", sys.exc_info()[0])
    data = config._sections

    ##creat a json file under the folder and write json data in 
    try:
      jsonFile = open("ini2json.json","w")
    except OSError as error:
      print ('Handling create json file error:',error)
    except:
      print ("Unexpected error:", sys.exc_info()[0])
    else:
      json.dump(data,jsonFile)
      jsonFile.close()

def yaml2json(yamlFile_Location):
    '''
    #Description:
      #Parser yaml file to json file
      #users should input a yaml file's location
      #this function will create yaml2json.json under the same folder
    #Args:
      #yamlFile_Location: the location of the yaml file to parse
    #Returns:
      #NULL
    #Raises:
      #OSError: A error occurred while open the yaml file 
      #Unexpected error: read the error info
    '''
    ##get yaml data and transform to json data
    try:
      yaml_stream = open(yamlFile_Location,'r')
    except OSError as error:
      print ('Handling open yaml file error:',error)
    except:
      print ("Unexpected error:", sys.exc_info()[0]) 

    data = yaml.load(yaml_stream)
    yaml_stream.close()

    ##creat a json file under the folder and write json data in 
    try:
      jsonFile = open("yaml2json.json","w")
    except OSError as error:
      print ('Handling create json file error:',error)
    except:
      print ("Unexpected error:", sys.exc_info()[0])
    else:
      json.dump(data,jsonFile)
      jsonFile.close()
     