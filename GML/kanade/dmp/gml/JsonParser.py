'''
Created on 2018/05/08

@author: R&D
'''

import json;

'''
    json
        featrues
            KEY_HEADER + {number}
        properties
            geometry
                coordinates
    
    see http://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-L01-v2_4.html
'''
class GMLParser(object):

    COLUMN_MAX = 73
    COLUMN_NUMBER_LENGTH = 3
    
    KEY_HEADER = "L01_"
    KEY_FEATRUES = "features"
    KEY_PROPERTYES = "properties"
    KEY_GEOMETRY = "geometry"
    KEY_COORDINATEDS = "coordinates"
    
    SCHEMA_PRICE = 6
    SCHEMA_STATE = 25
    SCHEMA_STATEDETAIL = 44
    
    LIST_LONGITUDE = 0
    LIST_LATITUDE = 1
    
    def __init__(self):
        '''
        Constructor
        '''
    
    '''
        set directory of file.
    '''
    def setDirectory(self, directory):
        self.directory = directory
    
    '''
        set name of file.
        and parse file as json.
    '''
    def parse(self, name):
        object = json.load(open(self.directory + '/' + name, encoding='utf8'))
        collection = object[GMLParser.KEY_FEATRUES]
        
        for element in collection:
            self.parseElement(element);
        
        return None;
    
    '''
        
    '''
    def parseElement(self, element):
        properties = element[GMLParser.KEY_PROPERTYES]
        
        key = GMLParser.KEY_HEADER + str(GMLParser.SCHEMA_STATE).zfill(GMLParser.COLUMN_NUMBER_LENGTH)
        list = properties[key].split(',');
        
        for index in range(len(list)):
            print(list[index])
        
        return None;
    
    '''
        
    '''
    def parseElements(self, element):
        properties = element[GMLParser.KEY_PROPERTYES]
        
        list = []
        
        for index in range(GMLParser.COLUMN_MAX):
            key = GMLParser.KEY_HEADER + str(index + 1).zfill(GMLParser.COLUMN_NUMBER_LENGTH)
            
            if (index + 1 == GMLParser.SCHEMA_PRICE or 
                index + 1 == GMLParser.SCHEMA_STATE or 
                index + 1 == GMLParser.SCHEMA_STATEDETAIL):
                list.append(properties[key])
        
        geometry = element[GMLParser.KEY_GEOMETRY]
        point = geometry[GMLParser.KEY_COORDINATEDS]
        latitude = point[GMLParser.LIST_LATITUDE]
        longitude = point[GMLParser.LIST_LONGITUDE]
        
        # list.append(latitude)
        # list.append(longitude)
        # temp = [str(value) for value in list]
        print("\t".join(list) + "\t" + str(latitude) + "\t" + str(longitude))
        
        return None;