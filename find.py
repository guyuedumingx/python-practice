import xlrd
import os 


class ReadSheet() : 

    def __init__(self) :
        pass  

    def Readdir(self, dir):
        return os.listdir(dir)

    def __ReadSheet(self, pos):
        try:
            return xlrd.open_workbook(pos)
        except:
            pass

    def __ReadTable (self, data, num) :
        try:
            return  data.sheets()[num]
        except:
            pass

    def getTable (self, file_name, numsheet):
         data = self.__ReadSheet(file_name)
         table = self.__ReadTable(data, numsheet)
         return table

class HandleSheet() :

    def __init__(self,) :
        pass

    def getNrow(self,table,row) :
        try:
            return table.row_values(row)
        except:
            return []

    def getCol(self, table, col) :
        try:
            return table.col_values(col)
        except:
            return []

    def find(self, data, name):
        i = 0
        for i in range(len(data)):
            if (data[i] == name):
                return i
        return -1

    def getCell (self, sheet,row, col) :
        return sheet.cell_value(row,col)

    def listFind (self , names, row_data):
        res = {}
        for name in names :
            try :
                row = self.find(row_data,name)
                res[name] = row  
            except:
                pass
        return res 

class InOut() :
    def __init__(self) :
        pass

    def prt(self, res, file) :
        for key,value in res.items():
            if (value != -1):
                print( file + '    第' + str(value+1)  +"行")
                row_data = handlesheeet.getCell(table,value,6)
                print(key +"\t" + row_data)

    def read(self) :
        class_name = input("请输入课程：")
        return class_name.split(',')
        





dir = '/home/harden/python-practice/123/'
inout = InOut()
names = inout.read()
readsheet = ReadSheet()
files = readsheet.Readdir(dir)

for file in files:
    table = readsheet.getTable(file,0)
    handlesheeet = HandleSheet()
    col_data = handlesheeet.getCol(table,0)
    if (len(col_data) == 0) :
        continue
    res = handlesheeet.listFind(names,col_data)   
    inout.prt(res, file) 











