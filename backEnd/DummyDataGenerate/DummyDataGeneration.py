# Importing Builtin Libraries
import sys
import string
import random
import pandas as pd
from pandas import DataFrame
#sys.path.append('C:/Users/Utkarsh Khursale/relationalDBManagementSystem')

# Importing User defined Modules
from backEnd.SQLConnectors.sqlConnector import executeGetCommand, executeInsertCommand
from backEnd.DummyDataGenerate.dummyDataPayload import *
from backEnd.propertyFiles.EnvironmentVariables import *
from backEnd.propertyFiles.Names import *
from backEnd.Utilities.utility import *
from backEnd.Utilities.SendEmailNotification.sendEmail import sendMailUsingSMTP
from backEnd.Processors.Encrypters.Encryption import wrapperEncryptFunction, wrapperDecyptFunction

# THIS FUNCTION WILL RETURN ENCRYPTED VALUES FOR PII DATA FOR DUMMY DATA
def getEnctryptedValuesForPII(reqPIIList):

    encryptedPIIData = []

    # GO THOUGH LOOP OF COLOUMNS AND ENCRYPT VALUES
    for index, colValue in enumerate(reqPIIList):

        # GET ENCRYPTED VALUE OF COLOUMN FROM PIIDATA
        encryptedPIIValue = wrapperEncryptFunction(colValue)

        # APPEND IT TO ENCRYPTED ARRAY
        encryptedPIIData.append(encryptedPIIValue)


    return encryptedPIIData

# THIS FUNCTION WILL CREATE A CSV FILE AT A FIXED LOCATION WITH THE STUDENT DETAILS
def getStudentDetailsCSV(coloumnsRequestedFromWeb, companyId):

    # This variable will contain all coloumns - FIXED + REQUESTED
    coloumnToBeFetched=getAllColoumnstoFetch(coloumnsRequestedFromWeb)

    reqColStr = getListOfStrings(coloumnToBeFetched)

    # Get the List of Interested Students from CSV provided as INPUT
    interestedStudents = setInterestedStudentsFromCSV(companyId)
    print(interestedStudents)
    # Store a Query to be Executed to fetch the Coloumns from DB for Interested Students
    executeSQ = SELECT_QUERY.format(reqColStr,TABLE_NAME,interestedStudents)
    resoverall = executeGetCommand(executeSQ)

    # Create a DataFrame of the returned result
    EncryptedDataFrame = DataFrame(resoverall,columns = coloumnToBeFetched)

    decryptedDataFrame = EncryptedDataFrame

    # LOOP over DataFrame from DB to decrypt the encrypted values in DB
    for rowIndex, row in EncryptedDataFrame.iterrows():

        for colIndex,col in enumerate(coloumnToBeFetched):

            if col in PII_COL_LIST:

                decryptedDataFrame.iloc[rowIndex,colIndex] = wrapperDecyptFunction(row[col])
            else:

                decryptedDataFrame.iloc[rowIndex,colIndex] = row[col]

    # Release Memory
    EncryptedDataFrame = DataFrame()

    decryptedDataFrame.to_csv(PATH_TO_CSV_FILE)

def getLowerUpperBounds():
        # COMMAND TO GET LOWERBOUND
        getLowerBoundCmd = GET_LOWER_BOUND_QUERY.format(TABLE_NAME)

        # GET LOWERBOUND
        maxValueInDB = executeGetCommand(getLowerBoundCmd)

        # RETURNS A TUPLE - GET FIRST ELEMENT
        if maxValueInDB[0][0] == None:
            lowerBound = 0
        else:
            lowerBound = maxValueInDB[0][0] + 1
        upperBound = lowerBound + NUMBER_OF_DUMMY_DATA_TOBE_INSERTED
        return [lowerBound,upperBound]

def insertDummyData():

        bounds = getLowerUpperBounds()
        lowerBound = bounds[0]
        upperBound = bounds[1]

        # Get command Executed
        commandString = ""
        templateString = "{}"
        comma = ","

        # RUN FOR LOOP TO GENERATE DUMMY DATA -- ROW WISE
        # DYNAMIC NUMBER IS BASICALLY ROW_NUMBER
        for rowValue in range (lowerBound, upperBound):
            # CREATE RANDOM ALPHANUMERIC EMAIL FOR INSERTION
            firstnameid = firstname.format(getFirstname())
            surnameid = surname.format(getSurname())
            rollnumberid = rollNumber.format(getRollno())
            registrationNo = registrationId.format(getRandomNum(REGISTRATION_NUMBER_LENGTH))
            emailid = email.format(getRandomAlphaNum(EMAIL_PREFIX_LENGTH))
            aadharid = aadhar.format(getRandomNum(AADHAR_LENGTH))
            mobileid = mobileNumber.format(getRandomNum(MOBILE_LENGTH))
            panid = PAN.format(getRandomAlphaNum(PAN_LENGTH))
            passid = passport.format(getRandomAlphaNum(PASSPORT_LENGTH))
            perAdd = permanantAddress.format(getAddress(ADDRESS_LENGTH))
            resAdd = residentialAddress.format(getAddress(ADDRESS_LENGTH))

            # Selecting 10th and 12 th Grade
            RandomGrade_10 = getMarks()
            RandomGrade_12 = getMarks()

            # 1st to 6th sem cgpas'
            firstCGPA = getCgpa()
            secondCGPA = getCgpa()
            thirdCGPA = getCgpa()
            fourthCGPA = getCgpa()
            fifthCGPA = getCgpa()
            sixthCGPA = getCgpa()

            InitialName = getFirstname()
            MiddleName = getFatherName()
            MotherInitial = getMotherName()
            FamilyName = getSurname()
            regisId = getRegistrationId()

            # INITIALISE EMPTY ENCRYPTED ARRAY TO STORE ENCRYPTED VALUES OF 9 COLOUMNS
            reqPIIList = []
            reqPIIList.append(firstnameid)

            reqPIIList.extend((surnameid,emailid,mobileid,aadharid,panid,passid,perAdd,resAdd))

            encrypted = getEnctryptedValuesForPII(reqPIIList)

            # INITIALISE 42 COLOUMNS LENTH STRING TO FILL UP VALUES
            templateString = """("{}",{},"{}","{}","{}","{}","{}","{}","{}","{}",{},{},{},{},"{}","{}","{}","{}",{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})"""
            commandString = commandString + templateString.format(registrationId.format(ID[regisId].format(registrationNo)),int(rollNumber.format(rollnumberid)),encrypted[0],encrypted[1],encrypted[2],
                                                                  encrypted[3],encrypted[4],encrypted[5],encrypted[6],nationality,isAadhar,isPAN,isPassport,isIndian,
                                                                  fathersName.format(MiddleName),mothersName.format(MotherInitial),encrypted[7],encrypted[8],
                                                                  tenthCGPA,twelthCGPA,tenthGrade.format(RandomGrade_10),twelthGrade.format(RandomGrade_12),firstSemCGPA.format(firstCGPA),secondSemCGPA.format(secondCGPA),
                                                                  thirdSemCGPA.format(thirdCGPA),fourthSemCGPA.format(fourthCGPA),fifthSemCGPA.format(fifthCGPA),sixthSemCGPA.format(sixthCGPA),seventhSemCGPA,eightthSemGCPA,
                                                                  isDiploma,diplomaMarks,isBacklog,numberOfBacklogs,activeBacklog,PassiveBacklog,isYD,YDYears,isEducationGap,educationGapYears,isPICTStudent,currentBatch)

            # ADD COMMA AFTER EVERY ROW BUT LAST ONE
            if(rowValue<upperBound-1):
                commandString = commandString + ","
            else:
                commandString = commandString + ";"

        # print(INSERT_DATA_QUERY.format(TABLE_NAME,COLOUMN_NAMES,commandString))

        # Execute Command to Insert Values
        result = executeInsertCommand(INSERT_DATA_QUERY.format(TABLE_NAME,COLOUMN_NAMES,commandString))

        # Sample of Rows inserted
        print("Total rows inserted {}".format(NUMBER_OF_DUMMY_DATA_TOBE_INSERTED))

def calculateCgpa():
    sql_select_query = "select firstSemCGPA,secondSemCGPA,thirdSemCGPA,fourthSemCGPA,fifthSemCGPA,sixthSemCGPA,seventhSemCGPA,eightthSemGCPA,registrationId from studentdetails"
    records = executeGetCommand(sql_select_query)
    for row in records:
        colName = 'CGPA'
        count=0
        num=0
        den=0
        credit=[25,25,25,25,23,23,22,22]
        for i in row:
            if i!=0 and i!= None and type(i) == float:
                num = num + i*credit[count]
                den = den+credit[count]
            else:
                regId=i
            count=count+1
        if den!=0:
            CGPA=num/den
        else:
            CGPA=0
        sql_update_query = UPDATE_QUERY.format(TABLE_NAME, colName, CGPA, regId)
        records1 = executeInsertCommand(sql_update_query)

def getGender():
    colName = 'Gender'
    sql_select_query = "select firstName,registrationId from studentdetails"
    records = executeGetCommand(sql_select_query)
    M_gender="M"
    F_gender="F"
    for row in records:
        firstname = wrapperDecyptFunction(row[0])
        regId = row[1]
        if firstname in MALE_NAME_LIST:
            sql_update_query = UPDATE_QUERY.format(TABLE_NAME, colName, M_gender, regId)
            print(sql_update_query)
            records1 = executeInsertCommand(sql_update_query)
        else:
            sql_update_query = UPDATE_QUERY.format(TABLE_NAME, colName, F_gender, regId)
            print(sql_update_query)
            records1 = executeInsertCommand(sql_update_query)

def getBranch():
    colName = 'Branch'
    sql_select_query = "select registrationId from studentdetails"
    records = executeGetCommand(sql_select_query)
    C_Branch = "CE"
    I_Branch = "IT"
    E_Branch = "ENTC"
    for row in records:
        for i in row:
            regId = i
            if i[0] == 'C':
                sql_update_query = UPDATE_QUERY.format(TABLE_NAME, colName, C_Branch, regId)
                print(sql_update_query)
                records1 = executeInsertCommand(sql_update_query)
            elif i[0] == 'I':
                sql_update_query = UPDATE_QUERY.format(TABLE_NAME, colName, I_Branch, regId)
                print(sql_update_query)
                records1 = executeInsertCommand(sql_update_query)
            else:
                sql_update_query = UPDATE_QUERY.format(TABLE_NAME, colName, E_Branch, regId)
                print(sql_update_query)
                records1 = executeInsertCommand(sql_update_query)


if __name__ == '__main__':
    pass
    #getBranch()
    #getGender()
    #calculateCgpa()
    # insertDummyData()
    # getStudentDetailsCSV(["fifthSemCGPA"])
    # sendMailUsingSMTP()
