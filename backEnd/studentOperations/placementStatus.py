from backEnd.propertyFiles.EnvironmentVariables import *
from backEnd.SQLConnectors.sqlConnector import executeGetCommand, executeInsertCommand
import datetime


def update_status(RegId):
    RegIdString = "'" + RegId + "'"
    sql_select_query = "SELECT * FROM companyDetails"
    CMP_COL_NAMES = "isApplied,isSelected,isPlaced"
    cmprecords = executeGetCommand(sql_select_query)
    cmprecordlist=[]
    for row in cmprecords:
        cmprowlist = list(row)
        cmprecordlist.append(cmprowlist)
    Id = 'registrationId'
    for r in cmprecordlist:
        studentrecordlist = []
        sql_select_student_query =  "SELECT {} FROM {}".format(Id,r[0])
        studentrecords = executeGetCommand(sql_select_student_query)
        for row in studentrecords:
            studentrecordlist.append(row[0])
        if RegId in studentrecordlist:
            sql_select_student_info = SELECT_QUERY.format(CMP_COL_NAMES,r[0],RegIdString)
            studentInforecords = executeGetCommand(sql_select_student_info)
            if studentInforecords == [(1,0,0)] :
                r.append('Applied')
            elif studentInforecords == [(1,1,0)] :
                r.append('Selected for next round')
            elif studentInforecords == [(1,-1,0)] :
                r.append('Not Selected for next round')
            elif studentInforecords == [(1,1,1)] :
                r.append('Placed')
            elif studentInforecords == [(1,-1,-1)] :
                r.append('Not Placed')
        else :
            r.clear()
    for row in cmprecords:
        a = datetime.datetime.now()
        ppt=row[9]
        test=row[10]
        tech=row[11]
        hr=row[12]
        diff1 = a-ppt
        diff2 = a-test
        diff3 = a-tech
        diff4 = a-hr
        if diff1.total_seconds() < 0 :
            round = "Pre-Placement Talk"
            round_timing = ppt
        else:
            if diff2.total_seconds() < 0 :
                round = "Aptitude Test"
                round_timing = test
            else:
                if diff3.total_seconds() < 0 :
                    round = "Technical Interview"
                    round_timing = tech
                else:
                    if diff4.total_seconds() < 0 :
                        round = "HR Interview"
                        round_timing = hr
                    else:
                        round = "Coming Soon"
                        round_timing = row[7]
        roundName = "roundName"
        timing = "timing"
        sql_update_query = UPDATE_QUERY2.format(TABLE_NAME2, roundName, round, row[0])
        records = executeInsertCommand(sql_update_query)
        sql_update_query2 = UPDATE_QUERY2.format(TABLE_NAME2, timing, round_timing, row[0])
        records2 = executeInsertCommand(sql_update_query2)

    return cmprecordlist
