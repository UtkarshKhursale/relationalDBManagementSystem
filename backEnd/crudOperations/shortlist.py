from backEnd.propertyFiles.EnvironmentVariables import *
from backEnd.Utilities.utility import *
from backEnd.SQLConnectors.sqlConnector import executeGetCommand, executeInsertCommand
from backEnd.Processors.Encrypters.Encryption import wrapperDecyptFunction, wrapperEncryptFunction
import pandas as pd

def update_shortlist(companyName,listType):
    dg = pd.read_csv(INTERESTED_STUDENTS_FILE_PATH)
    sql_update_query1 = "UPDATE {} SET {} = '{}'".format(companyName, listType, -1)
    records = executeInsertCommand(sql_update_query1)
    for index, row in dg.iterrows():
        regId =row[0]
        sql_update_query = UPDATE_QUERY.format(companyName, listType, 1, regId)
        records = executeInsertCommand(sql_update_query)
        if listType == "isPlaced":
            sql_update_query2 = UPDATE_QUERY.format(TABLE_NAME, listType, 1, regId)
            records2 = executeInsertCommand(sql_update_query2)
