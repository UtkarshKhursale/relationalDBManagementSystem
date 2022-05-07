import sys
# from backEnd.SQLConnectors.sqlConnector import executeGetCommand

PROJECT_NAME = "relationalDBManagementSystem"


# THIS FUNCTION WILL RETURN BASE DIRECTORY - PROJECT DIRECTORY
def getBaseDir():

    BASE_DIR = ''
    flag = True
    for path in sys.path:
        possibleProjectName = path.split("\\")[-2]
        print(possibleProjectName)
        if (PROJECT_NAME==possibleProjectName):
            BASE_DIR = path
            flag = False
            break

    if(flag):
        print("Failed to SET BASE_DIR. Please follow Instructions from resource.txt File")
    else:
        print("Your BASE_DIR is SET to: {} ".format(BASE_DIR))

    return BASE_DIR

# # GET COLOUMNS
# def getColoumns():
#     GET_COLOUMNS_QUERY="SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'StudentDetails';"
#     coloumnNames = executeGetCommand(GET_COLOUMNS_QUERY)
#     coloumnList = []
#     for item in coloumnNames:
#         coloumnList.append(item[0])
#     coloumnList="\""+",".join(coloumnList)+"\""
#     print(coloumnList)
# getColoumns()
