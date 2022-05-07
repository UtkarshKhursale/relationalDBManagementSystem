from backEnd.propertyFiles.EnvironmentVariables import *
from backEnd.SQLConnectors.sqlConnector import executeGetCommand, executeInsertCommand


def delete_table_row(stuRegId):
    sql_delete_query = DELETE_QUERY.format(TABLE_NAME,stuRegId)
    records = executeInsertCommand(sql_delete_query)
    return records
