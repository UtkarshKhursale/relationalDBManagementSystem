from backEnd.propertyFiles.EnvironmentVariables import *
from backEnd.Utilities.utility import *
from backEnd.SQLConnectors.sqlConnector import executeGetCommand, executeInsertCommand
from backEnd.Processors.Encrypters.Encryption import wrapperDecyptFunction, wrapperEncryptFunction
import pandas as pd

def create_table() :
    newEntryList = []
    toConvertToString="'{}'"
    templateString = """("{}",{},"{}","{}","{}","{}","{}","{}","{}","{}",{},{},{},{},"{}","{}","{}","{}",{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})"""
    dg = pd.read_csv(INTERESTED_STUDENTS_FILE_PATH)
    #records = 1
    for index, row in dg.iterrows():
        #print(row[4])
        newEntryList.append(templateString.format(row[0],row[1],wrapperEncryptFunction(row[2]),wrapperEncryptFunction(row[3]),wrapperEncryptFunction(row[4]),
                                                  wrapperEncryptFunction(str(row[5])),wrapperEncryptFunction(str(row[6])),wrapperEncryptFunction(str(row[7])),
                                                  wrapperEncryptFunction(str(row[8])),row[9],row[10],row[11],row[12],row[13],row[14],row[15],
                                                  wrapperEncryptFunction(row[16]),wrapperEncryptFunction(row[17]),row[18],row[19],row[20],
                                                  row[21],row[22],row[23],row[24],row[25],row[26],row[27],row[28],row[29],row[30],row[31],
                                                  row[32],row[33],row[34],row[35],row[36],row[37],row[38],row[39],row[40],row[41],))
    newEntryString = getListOfStrings(newEntryList)
    sql_insert_query = INSERT_DATA_QUERY.format(TABLE_NAME, COLOUMN_NAMES, newEntryString)
    records = executeInsertCommand(sql_insert_query)
    return records
