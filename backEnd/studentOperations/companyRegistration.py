from backEnd.propertyFiles.EnvironmentVariables import *
from backEnd.SQLConnectors.sqlConnector import executeGetCommand, executeInsertCommand
from backEnd.studentOperations.readCompanies import read_company_table

def create_company_table(companyId):
    sql_create_query = CREATE_TABLE_QUERY.format(companyId)
    records = executeInsertCommand(sql_create_query)
    return records

def insert_company_table(RegId,companyId):
    CMP_COL_NAMES = "registrationId,isApplied,isSelected,isPlaced"
    newEntryString = """("{}",{},{},{})""".format(RegId,1,0,0)
    sql_insert_query = INSERT_DATA_QUERY.format(companyId, CMP_COL_NAMES, newEntryString)
    records = executeInsertCommand(sql_insert_query)
    return records


def applied_check(RegId):
    rtable = read_company_table(RegId)
    appliedlist = []
    Id = 'registrationId'
    for r in rtable:
        recordlist = []
        sql_select_query =  "SELECT {} FROM {}".format(Id,r[0])
        records = executeGetCommand(sql_select_query)
        for row in records:
            recordlist.append(row[0])
        if RegId not in recordlist:
            appliedlist.append(True)
        else:
            appliedlist.append(False)
    return appliedlist
