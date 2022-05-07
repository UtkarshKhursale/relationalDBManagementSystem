from backEnd.propertyFiles.EnvironmentVariables import *
from backEnd.SQLConnectors.sqlConnector import executeGetCommand
import datetime

def read_company_table(regId) :
    stuRegIdString = "'" + regId + "'"
    col_names = "Branch,CGPA,isPlaced"
    sql_select_student_query = SELECT_QUERY.format(col_names,TABLE_NAME,stuRegIdString)
    student_records = executeGetCommand(sql_select_student_query)
    for row in student_records:
        branch = row[0]
        CGPA = row[1]
        isPlaced = row[2]
    sql_select_query = "SELECT * FROM companyDetails"
    records = executeGetCommand(sql_select_query)
    recordlist=[]

    for row in records:
        a = datetime.datetime.now()
        b=row[7]
        diff = a-b
        if  diff.total_seconds() < 0 and CGPA > row[3] and branch in row[2] and isPlaced!=1 :
            rowlist = list(row)
            recordlist.append(rowlist)

    return recordlist

def read_company_name():
    sql_select_query = "SELECT companyId,companyName FROM companyDetails"
    records = executeGetCommand(sql_select_query)
    return records
