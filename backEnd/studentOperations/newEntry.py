from backEnd.Processors.Encrypters.Encryption import wrapperDecyptFunction, wrapperEncryptFunction
from backEnd.SQLConnectors.sqlConnector import executeGetCommand, executeInsertCommand
from backEnd.propertyFiles.EnvironmentVariables import *


def newEntry(regId, fname, lname, email, mobno, batch, branch):
    stdEntryString = """("{}",{},"{}","{}","{}","{}","{}",{},"{}")""".format(regId,0,wrapperEncryptFunction(fname),wrapperEncryptFunction(lname),wrapperEncryptFunction(email),wrapperEncryptFunction(mobno),"0",batch,branch)
    newColumnNames = "registrationId,rollNumber,firstName,surName,email,mobileNumber,aadhar,currentBatch,Branch"
    sql_insert_query = INSERT_DATA_QUERY.format(TABLE_NAME, newColumnNames, stdEntryString)
    records = executeInsertCommand(sql_insert_query)
    return records
