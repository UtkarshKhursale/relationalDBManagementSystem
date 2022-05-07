from backEnd.propertyFiles.EnvironmentVariables import *
from backEnd.SQLConnectors.sqlConnector import executeGetCommand
from backEnd.Processors.Encrypters.Encryption import wrapperDecyptFunction, wrapperEncryptFunction

def read_table(stuRegId):
    stuRegIdString = "'" + stuRegId + "'"
    sql_select_query = SELECT_QUERY.format(COLOUMN_NAMES,TABLE_NAME,stuRegIdString)
    records = executeGetCommand(sql_select_query)
    for row in records:
        rowlist = list(row)
        if row[2]:
            rowlist[2]=wrapperDecyptFunction(row[2])
        if row[3]:
            rowlist[3]=wrapperDecyptFunction(row[3])
        if row[4]:
            rowlist[4]=wrapperDecyptFunction(row[4])
        if row[5]:
            rowlist[5]=wrapperDecyptFunction(row[5])
        if row[6] and row[6] != '0' :
            rowlist[6]=wrapperDecyptFunction(row[6])
        if row[7]:
            rowlist[7]=wrapperDecyptFunction(row[7])
        if row[8]:
            rowlist[8]=wrapperDecyptFunction(row[8])
        if row[16]:
            rowlist[16]=wrapperDecyptFunction(row[16])
        if row[17]:
            rowlist[17]=wrapperDecyptFunction(row[17])
    rowtuple=tuple(rowlist)
    recordlist=[]
    recordlist.append(rowtuple)

    return recordlist
