from backEnd.propertyFiles.EnvironmentVariables import *
from backEnd.SQLConnectors.sqlConnector import executeGetCommand, executeInsertCommand
from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import pickle
from datetime import datetime
import time


def insert_company(companyId,companyName,branchCriteria,cgpaCriteria,jobRole,package,visitDate,reg_expiry):
    COMPANY_COL_NAMES = "companyId,companyName,branchCriteria,cgpaCriteria,jobRole,package,visitDate,reg_expiry"
    valueString = """("{}","{}","{}",{},"{}",{},"{}","{}")""".format(companyId,companyName,branchCriteria,float(cgpaCriteria),jobRole,float(package),visitDate,reg_expiry)
    sql_insert_query = INSERT_DATA_QUERY.format(TABLE_NAME2, COMPANY_COL_NAMES, valueString)
    records = executeInsertCommand(sql_insert_query)
    return records

def update_timings(companyId, startColName, roundStartTime, roundEndTime):
    sql_update_query = UPDATE_QUERY2.format(TABLE_NAME2, startColName, roundStartTime, companyId)
    records = executeInsertCommand(sql_update_query)
    companyName = "companyName"
    sql_select_query = SELECT_QUERY2.format(companyName, TABLE_NAME2, companyId)
    records2 = executeGetCommand(sql_select_query)
    for row in records2:
        company = row[0]

    if startColName == "pptTime":
        eventName = "Pre-Placement Talk"
    elif startColName == "testTime":
        eventName = "Aptitude Test"
    elif startColName == "techIntTime":
        eventName = "Technical Interview"
    elif startColName == "HRIntTime":
        eventName = "HR Interview"
    else:
        eventName = "No event"
    TOKEN_PATH = BASE_DIR + "\\token.pkl"
    credentials = pickle.load(open(TOKEN_PATH, "rb"))
    service = build("calendar", "v3", credentials = credentials)
    calendar_id = '15b6dnggoq9mgbfibm6so5bnkg@group.calendar.google.com'
    event = {
    'summary': company +" " + eventName,
    'location': 'IT Seminar Hall',
    'description': company,
    'start': {
        'dateTime': roundStartTime + ':00',
        'timeZone': 'Asia/Kolkata',
        },
    'end': {
        'dateTime': roundEndTime + ':00',
        'timeZone': 'Asia/Kolkata',
        },
    'attendees': [
        {'email': 'varadd15032000@gmail.com'},
        ],
    'reminders': {
        'useDefault': False,
    'overrides': [
        {'method': 'email', 'minutes': 10},
        {'method': 'popup', 'minutes': 10},
        ],
        },
        }
    sendUpdate ="all"

    event = service.events().insert(calendarId=calendar_id, body=event, sendUpdates = sendUpdate).execute()

    return records
