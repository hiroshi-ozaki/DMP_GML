'''
Created on 2018/04/19

@author: R&D
'''

# module name is "FileName", 
# class name is "ClassName"

# from package.module import class
import datetime
from kanade.dmp.gml.JsonParser import GMLParser

if __name__ == '__main__':
    
    print(datetime.datetime.today())
    
    parser = GMLParser();
    parser.setDirectory("C:/Data/Document/07.R&D/DMP/log/opendata/L01-18_00_GML");
    parser.parse("L01-18.geojson");