import sys
import os
import shutil

sys.path.append('C:/Users/Utkarsh Khursale/relationalDBManagementSystem')
# ==============================================================
# ======================= USER IMPORTS =========================
# ==============================================================
from django.shortcuts import render
from django.http import FileResponse
from django.core.files.storage import FileSystemStorage
from backEnd.DummyDataGenerate.DummyDataGeneration import getStudentDetailsCSV, calculateCgpa
from backEnd.Utilities.SendEmailNotification.sendEmail import sendMailUsingSMTP,sendMailUsingSMTPToUser
from rdbms.relationalDataBaseManagement.settings import *
from backEnd.Utilities.utility import deleteFilesInFolder,renameFile,saveFile,saveResumeFile,deleteFile,getListOfStrings
from backEnd.propertyFiles.EnvironmentVariables import *
from backEnd.crudOperations.create import create_table
from backEnd.crudOperations.shortlist import update_shortlist
from backEnd.crudOperations.read import read_table
from backEnd.crudOperations.update import update_table
from backEnd.crudOperations.delete import delete_table_row
from backEnd.crudOperations.insert_company import insert_company, update_timings
from backEnd.studentOperations.readCompanies import read_company_table, read_company_name
from backEnd.studentOperations.companyRegistration import create_company_table, insert_company_table, applied_check
from backEnd.studentOperations.placementStatus import update_status
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User


@user_passes_test(lambda u: u.is_superuser)
@login_required
def sent(request):
    return(render(request, "sent.html", {"text":"home"}))

@user_passes_test(lambda u: u.is_superuser)
@login_required
def index(request):
    if request.method=="POST":


        # TAKE INPUTS FROM HTML FROM A POST CALL
        inputFields = request.POST.getlist('inputFields')
        userEmail = request.POST.getlist('email')
        companyId = request.POST.getlist('company')



        # GET THE DETAILS OF INTERESTED STUDENTS
        getStudentDetailsCSV(inputFields, companyId)

        # SEND EMAIL TO DESIRED EMAIL
        # sendMailUsingSMTP()
        sendMailUsingSMTPToUser(userEmail)

        return(render(request, "sent.html", {"text":"Your Email was sent to:{}".format(getListOfStrings(userEmail))}))
    rtable = read_company_name()
    context= {
    'rtable': rtable,
            }
    return render(request, "index2.html",context)



@user_passes_test(lambda u: u.is_superuser)
@login_required
def crud(request):
	return render(request,'crudpage.html',)

@user_passes_test(lambda u: u.is_superuser)
@login_required
def create(request):
	return render(request,'create.html',)

@user_passes_test(lambda u: u.is_superuser)
@login_required
def create_submit(request):
	inputeCSVFile = request.FILES["studentInfo"]
	deleteFilesInFolder(INPUT_FOLDER_PATH)
	saveFile(inputeCSVFile,MEDIA_ROOT)
	newrecords = create_table()
	return render(request,'create_submit.html',)

@user_passes_test(lambda u: u.is_superuser)
@login_required
def read(request):
	return render(request,'read.html',)

@user_passes_test(lambda u: u.is_superuser)
@login_required
def read_submit(request):
	readRegId=request.POST['quantity']
	rtable = read_table(readRegId)
	context= {
        	'rtable': rtable,
			}
	return render(request,'read_submit.html', context)

@user_passes_test(lambda u: u.is_superuser)
@login_required
def update(request):
	return render(request,'update.html',)

@user_passes_test(lambda u: u.is_superuser)
@login_required
def update_submit(request):
	colName =request.POST['col']
	colValue =request.POST['value']
	regId =request.POST['quantity']
	#print(colName, colValue, regId)
	updatedrecords = update_table(colName, colValue, regId)
	context= {
        	'colName': colName,
			'colValue': colValue,
			'regId': regId,
			}
	return render(request,'update_submit.html', context)

@user_passes_test(lambda u: u.is_superuser)
@login_required
def delete(request):
	return render(request,'delete.html',)

@user_passes_test(lambda u: u.is_superuser)
@login_required
def delete_submit(request):
	deleteRegId=request.POST['quantity']
	deletedrecords = delete_table_row(deleteRegId)
	context= {
        	'deleteRegId': deleteRegId,
			}
	return render(request,'delete_submit.html', context)

@user_passes_test(lambda u: u.is_superuser)
@login_required
def add_company(request):
    return render(request,'addCompany.html',)

@user_passes_test(lambda u: u.is_superuser)
@login_required
def add_company_submit(request):
    companyId = request.POST.get('companyId')
    companyName = request.POST.get('companyName')
    branchCriteria = request.POST.getlist('branch')
    #branchCriteriaString = "[" + branch1 +","+ branch2 +","+ branch3 + "]"
    cgpaCriteria = request.POST.get('cgpaCriteria')
    jobRole = request.POST.get('jobRole')
    package = request.POST.get('package')
    visitDate = request.POST.get('visitDate')
    reg_expiry = request.POST.get('reg_expiry')
    newrecords = insert_company(companyId,companyName,branchCriteria,cgpaCriteria,jobRole,package,visitDate,reg_expiry)
    create_company_table(companyId)
    text  = "Company Added"
    return render(request,'addCompany_submit.html',{'text':text})

@user_passes_test(lambda u: u.is_superuser)
@login_required
def shortlist(request):
    rtable = read_company_name()
    context= {
    'rtable': rtable,
            }
    return render(request,'upload_shortlist.html',context)

@user_passes_test(lambda u: u.is_superuser)
@login_required
def shortlist_submit(request):
    companyName = request.POST.get('company')
    listType = request.POST.get('listtype')
    inputeCSVFile = request.FILES["studentInfo"]
    deleteFilesInFolder(INPUT_FOLDER_PATH)
    saveFile(inputeCSVFile,MEDIA_ROOT)
    update_shortlist(companyName, listType)
    text = "List Uploaded"
    return render(request,'shortlist_submit.html',{'text':text})

@user_passes_test(lambda u: u.is_superuser)
@login_required
def round_time(request):
    rtable = read_company_name()
    context= {
    'rtable': rtable,
            }
    return render(request,'round_time.html',context)

@user_passes_test(lambda u: u.is_superuser)
@login_required
def round_time_submit(request):
    companyId = request.POST.get('company')
    startColName = request.POST.get('round')
    roundStartTime = request.POST.get('startTime')
    roundEndTime = request.POST.get('endTime')
    update_timings(companyId, startColName, roundStartTime, roundEndTime)
    text = "Round Timing Updated"

    return render(request,'round_time_submit.html',{'text':text})

@login_required
def calendar(request):
	return render(request,'calendar.html',)

@login_required
def placement_status(request):
    RegId = request.user.username
    rtable = update_status(RegId)
    context= {
    'rtable': rtable,
            }
    return render(request,'placementStatus.html', context)

@login_required
def profile(request):
    RegId = request.user.username
    rtable = read_table(RegId)
    context= {
        	'rtable': rtable,
			}
    return render(request,'read_submit.html', context)

@login_required
def editprofile(request):
    return render(request,'editprofile.html')

@login_required
def update_profile(request):
    RegId = request.user.username
    for COL in COL_LIST:
        colValue =request.POST.get(COL)
        if colValue != '' and colValue != None and colValue != "":
            updatedrecords = update_table(COL, colValue, RegId)
    calculateCgpa()
    rtable = read_table(RegId)
    context= {
    'rtable': rtable,
            }
    return render(request,'read_submit.html', context)

@login_required
def companies(request):
    if request.method=="POST":
        RegId = request.user.username
        companyId = request.POST["button"]
        newrecords = insert_company_table(RegId,companyId)
        rtable = read_company_table(RegId)
        applied = applied_check(RegId)
        i=0
        for r in rtable:
            r.append(applied[i])
            i=i+1
        context= {
        'rtable': rtable,
            }
        return render(request,'companies.html', context)
    else:
        RegId = request.user.username
        rtable = read_company_table(RegId)
        applied = applied_check(RegId)
        i=0
        for r in rtable:
            r.append(applied[i])
            i=i+1
        context= {
        'rtable': rtable,
            }
        return render(request,'companies.html', context)


@login_required
def resume(request):
    return render(request,'resume.html',)

@login_required
def resume_view(request):
    if request.FILES.get("Resume") :
        inputeFile = request.FILES.get("Resume")
        RegId = request.user.username
        filename = RegId +"_resume.pdf"
        filepath = os.path.join(RESUME_ROOT, filename)
        deleteFile(filepath)
        saveResumeFile(inputeFile,RESUME_ROOT,filename)
        text = "Resume Uploaded"
        context= {
            	'text': text,
    			}
        return render(request,'resume_view.html',context)
    text = "Resume Not Uploaded"
    context= {
            'text': text,
            }
    return render(request,'resume_view.html',context)

@login_required
def resume_view_pdf(request):
    RegId = request.user.username
    filename = RegId +"_resume.pdf"
    filepath = os.path.join(RESUME_ROOT, filename)
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')
