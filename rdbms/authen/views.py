from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from backEnd.studentOperations.newEntry import newEntry

def home(request):
    return render(request, 'auth/home.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            stdRegId = user.username
            stdFname = user.first_name
            stdLname = user.last_name
            stdEmail = user.email
            stdMobNo = user.mobile_no
            stdBatch = user.batch
            stdBranch = user.branch
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            newrecords = newEntry(stdRegId,stdFname,stdLname,stdEmail,stdMobNo,stdBatch,stdBranch)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'auth/signup.html', { 'form' : form })
