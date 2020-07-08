import csv, io
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ObjectDoesNotExist
from .models import Student
from .forms import CreateUserForm

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            
            user = form.save()

            s = Student()
            s.user = user
            s.save()

            # messages.success(request,'Account was created for ' + user)
            return redirect('login')


    context = {'form' : form}
    return render(request, 'polls/register.html', context)

def upload(request):
    csv_file = request.FILES.get('file')
    unsaved = 0
    unsaved_str = ""
    template = "polls/upload.html"

    if csv_file is not None:
        if not csv_file.name.endswith('.csv'):
            messages.error(request, "This is not a csv file")

        data_Set = csv_file.read().decode('UTF-8')
        io_string = io.StringIO(data_Set)
        next(io_string)
    
        for column in csv.reader(io_string, delimiter=',', quotechar="|"):
            try:
                usr = User.objects.get(username = column[0])
            except ObjectDoesNotExist:
                usr = None
            
            if usr is not None:
                usr.student.nilai1 = column[1]
                usr.student.nilai2 = column[2]
                usr.student.nilai3 = column[3]
                usr.first_name = column[4]

                usr.is_active = True
                usr.save()
                usr.student.save()

            else:
                unsaved = unsaved + 1

    if unsaved > 0 :
        unsaved_str = "There are " + str(unsaved) + " unsaved data from previous upload"

    context = {
        'order' : 'Order of CSV should be nim, nilai1, nilai2, nilaiminggu3, rapot.',
        'unsaved' : unsaved_str
    }

    return render(request, template, context)


def leaderboard(request):
    template = "polls/leaderboard.html"
    return render(request, template)

def login(request):
    template = "polls/login.html"
    return render(request, template)

def nilai(request):
    current_user = request.user
    template = "polls/nilai.html"
    context = {
        'nilai': current_user.student.nilai1,
    }    
    return render(request, template, context)

def rapot(request):
    current_user = request.user
    template = "polls/rapot.html"
    context = {
        'nilai1': current_user.student.nilai1,
        'nilai2': current_user.student.nilai2,
        'nilai3': current_user.student.nilai3,
    }    
    return render(request, template, context)
