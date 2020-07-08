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
from django.conf.urls.static import static

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
                usr.first_name = column[1]
                usr.student.nilai1 = column[2]
                usr.student.nilai2 = column[3]
                usr.student.nilai3 = column[4]
                usr.student.nilai4 = column[5]
                usr.student.kepemimpinan = column[6]
                usr.student.nasionalisme = column[7]
                usr.student.kebermanfaatan = column[8]
                usr.student.keilmuan = column[9]
                usr.student.adaptif = column[10]
                usr.student.solidaritas = column[11]
                usr.student.kolaboratif = column[12]

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

def nilai(request):
    current_user = request.user
    template = "polls/nilai.html"
    context = {
        'nilai': current_user.student.nilai1,
        'kepemimpinan': current_user.student.kepemimpinan,
        'nasionalisme': current_user.student.nasionalisme,
        'kebermanfaatan': current_user.student.kebermanfaatan,
        'keilmuan': current_user.student.keilmuan,
        'adaptif': current_user.student.adaptif,
        'solidaritas': current_user.student.solidaritas,
        'kolaboratif': current_user.student.kolaboratif,
    }    
    return render(request, template, context)

def rapot(request):
    current_user = request.user
    template = "polls/rapot.html"
    context = {
        'kepemimpinan': current_user.student.kepemimpinan,
        'nasionalisme': current_user.student.nasionalisme,
        'kebermanfaatan': current_user.student.kebermanfaatan,
        'keilmuan': current_user.student.keilmuan,
        'adaptif': current_user.student.adaptif,
        'solidaritas': current_user.student.solidaritas,
        'kolaboratif': current_user.student.kolaboratif,
    }    
    return render(request, template, context)
