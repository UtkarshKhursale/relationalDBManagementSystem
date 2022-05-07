# Import Builtin Packges
import sys
import mysql.connector


# ==============================================================
# ======================= USER IMPORTS =========================
# ==============================================================
from backEnd.propertyFiles.EnvironmentVariables import HOST_NAME,DB_USER_NAME,DB_NAME,PORT_NAME,PASSWORD
from backEnd.Processors.Encrypters.Encryption import wrapperDecyptFunction
# DECRYPT PASSWORD TO OPEN SQL CONNECTION
decryptedPassword = wrapperDecyptFunction(PASSWORD)

# EXECUTE COMMAND TO INSERT VALUES
def executeInsertCommand(command):
    # Open SQL Connection
    sqlConnector = mysql.connector.connect(host=HOST_NAME, user=DB_USER_NAME, passwd=decryptedPassword, database=DB_NAME, port=PORT_NAME)
    mycursor = sqlConnector.cursor()

    # Execute Command
    mycursor.execute(command)

    # Insert into DB
    sqlConnector.commit()

    # Fetch from Table and return one Row
    returnOneRow = mycursor.fetchone()

    # Close the Connection
    mycursor.close()

    # Return one Row
    return returnOneRow

# EXECUTE COMMAND TO GET VALUES
def executeGetCommand(command):
    # Open SQL Connection
    sqlConnector = mysql.connector.connect(host=HOST_NAME, user=DB_USER_NAME, passwd=decryptedPassword, database=DB_NAME, port=PORT_NAME)
    mycursor = sqlConnector.cursor()

    # Execute Command
    mycursor.execute(command)

    # Fetch from Table and return one Row
    returnOneRow = mycursor.fetchall()

    # Close the Connection
    mycursor.close()

    # Return one Row
    return returnOneRow
