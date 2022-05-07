#===================================================================
#========================== Imports ================================
#===================================================================
import random
import string
import pandas as pd
import sys
import os
import shutil

# ==============================================================
# ======================= USER IMPORTS =========================
# ==============================================================

from backEnd.propertyFiles.Names import *
from django.core.files.storage import FileSystemStorage
from backEnd.propertyFiles.EnvironmentVariables import *
from backEnd.SQLConnectors.sqlConnector import executeGetCommand, executeInsertCommand

#=================================================================
#================== PII Data Generation ==========================
#=================================================================
def getFirstname():
    MaleFirstName = random.choice(MALE_NAME_LIST)
    FemaleFirstName = random.choice(FEMALE_NAME_LIST)
    ChoiceOfName = [MaleFirstName,FemaleFirstName]
    FinalFirstNameChoice = random.choice(ChoiceOfName)
    return FinalFirstNameChoice

def getFatherName():
    FatherName = random.choice(MALE_NAME_LIST)
    return FatherName

def getMotherName():
    MotherNameSelection = random.choice(FEMALE_NAME_LIST)
    return MotherNameSelection

def getSurname():
    SurName = random.choice(LAST_NAME_LIST)
    return SurName

#===================================================================
#========================== Marks Generation========================
#===================================================================
def getCgpa():
    firstCGPA = round(random.uniform(6.0, 10.0),1)
    return firstCGPA

def getMarks():
    RandomGrade = round(random.uniform(55.0, 99.9),1)
    return RandomGrade

#===================================================================
#=======================Dummy Data Generation ======================
#===================================================================

def getRegistrationId():
    regisId = random.randint(0,2)
    return regisId

def getRandomAlphaNum(len):
    return ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k = len))

def getRandomNum(len):
    return ''.join(random.choices(string.digits, k = len))

def getAddress(len):
    return ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k = len))

def getRollno():
    return random.randint(40000,49999)

#=====================Reading Interested Student File===========================
#=====================Converting Registrtion ID into ===========================
#=====================Comma Separated String Value =============================
def getListOfStrings(list):
    return ','.join(list)

def setInterestedStudentsFromCSV(companyId):
    list = []
    toConvertToString="'{}'"
    companyIdString = companyId[0]
    sql_select_query = "SELECT registrationId FROM {}".format(companyIdString)
    stu_records = executeGetCommand(sql_select_query)
    for row in stu_records:
        list.append(toConvertToString.format(row[0]))
    return getListOfStrings(list)

def getAllColoumnstoFetch(appendList):
    return MANDATORY_COL_TO_BE_SENT + appendList

#===================================================================
#================== File Related Operations =======================
#===================================================================

def deleteFilesInFolder(path):
    if os.path.exists(path):
        for root, dirs, files in os.walk(path):
            for f in files:
                os.unlink(os.path.join(root, f))
            for d in dirs:
                shutil.rmtree(os.path.join(root, d))

def renameFile():
    folder = INPUT_FOLDER_PATH
    for count, filename in enumerate(os.listdir(folder)):
        src =f"{folder}/{filename}"  # foldername/filename, if .py file is outside folder
        dst =f"{folder}/{FILE_NAME_OF_FILE_TOBE_PARSED}"
    os.rename(src, dst)

def saveFile(inputFileObject,fileLocation):
        fs = FileSystemStorage(location=fileLocation)
        filename = fs.save(inputFileObject.name, inputFileObject)
        file_url = fs.url(filename)
        renameFile()

def deleteFile(filepath):
    if os.path.exists(filepath):
        os.remove(filepath)

def saveResumeFile(inputFileObject,fileLocation,newname):
    fs = FileSystemStorage(location=fileLocation)
    filename = fs.save(inputFileObject.name, inputFileObject)
    file_url = fs.url(filename)
    renameResumeFile(newname)

def renameResumeFile(name):
    folder = RESUMES_FOLDER_PATH
    for count, filename in enumerate(os.listdir(folder)):
        src =f"{folder}/{filename}"  # foldername/filename, if .py file is outside folder
        dst =f"{folder}/{name}"
    os.rename(src, dst)
