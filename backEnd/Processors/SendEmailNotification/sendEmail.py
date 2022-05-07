import os
import sys
import base64
from datetime import date

# Sendgrid Dependencies
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (Mail, Attachment, FileContent, FileName, FileType, Disposition)

# SMTP Dependencies
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
import smtplib

#sys.path.append('C:\\Users\\lenovo\\data structure in python\\BE project\\relationalDBManagementSystem')
# from emailProperties import *
from backEnd.Processors.SendEmailNotification.emailProperties import *
from backEnd.propertyFiles.utility import getListOfStrings

def sendMailUsingSMTP():
    # Create a multipart message
    msg = MIMEMultipart()
    body_part = MIMEText(MESSAGE_BODY, 'plain')
    msg['Subject'] = EMAIL_SUBJECT.format(date.today())
    msg['From'] = EMAIL_FROM
    msg['To'] = getListOfStrings(EMAIL_TO)
    # Add body to email
    msg.attach(body_part)
    # open and read the CSV file in binary
    with open(PATH_TO_CSV_FILE,'rb') as file:
    # Attach the file with filename to the email
        msg.attach(MIMEApplication(file.read(), Name=FILE_NAME.format(date.today())))

    # Create SMTP object
    smtp_obj = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    smtp_obj.connect(SMTP_SERVER,SMTP_PORT)
    smtp_obj.ehlo()
    smtp_obj.starttls()
    smtp_obj.ehlo()
    # Login to the server
    smtp_obj.login(SMTP_USERNAME, SMTP_PASSWORD)

    # Convert the message to a string and send it
    smtp_obj.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
    smtp_obj.quit()

def sendMailUsingSMTPToUser(userEmail):
    # Create a multipart message
    msg = MIMEMultipart()
    body_part = MIMEText(MESSAGE_BODY, 'plain')
    msg['Subject'] = "TNP made Easy StudentDetails | {}".format(date.today())#EMAIL_SUBJECT.format(date.today())
    msg['From'] = EMAIL_FROM
    msg['To'] = getListOfStrings(userEmail)
    # Add body to email
    msg.attach(body_part)
    # open and read the CSV file in binary
    with open(PATH_TO_CSV_FILE,'rb') as file:
    # Attach the file with filename to the email
        msg.attach(MIMEApplication(file.read(), Name=FILE_NAME.format(date.today())))

    # Create SMTP object
    smtp_obj = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    smtp_obj.connect(SMTP_SERVER,SMTP_PORT)
    smtp_obj.ehlo()
    smtp_obj.starttls()
    smtp_obj.ehlo()
    # Login to the server
    smtp_obj.login(SMTP_USERNAME, SMTP_PASSWORD)

    # Convert the message to a string and send it
    smtp_obj.sendmail(EMAIL_FROM, userEmail, msg.as_string())
    smtp_obj.quit()
