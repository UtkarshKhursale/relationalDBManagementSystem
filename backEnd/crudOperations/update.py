from backEnd.propertyFiles.EnvironmentVariables import *
from backEnd.SQLConnectors.sqlConnector import executeGetCommand, executeInsertCommand
from backEnd.Processors.Encrypters.Encryption import wrapperDecyptFunction, wrapperEncryptFunction


def update_table(colName, colValue, regId):
    #ENCRYPTED_COL_LIST = ['email','mobileNumber','aadhar','PAN','passport','permanantAddress','residentialAddress']
    if colName in PII_COL_LIST :
        colValue = wrapperEncryptFunction(colValue)
    sql_update_query = UPDATE_QUERY.format(TABLE_NAME, colName, colValue, regId)
    records = executeInsertCommand(sql_update_query)
    #print(records)
    return records
