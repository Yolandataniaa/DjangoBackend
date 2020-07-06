import csv, io
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from django.template import loader
from .models import Student
from django.contrib.auth.models import User
# from .models import NilaiMinggu1
# from .models import NilaiMinggu2
# from .models import NilaiMinggu3

# Create your views here.

def upload(request):

    template = "polls/upload.html"

    context = {
        'order' : 'Order of CSV should be nim, nilai1, nilai2, nilaiminggu3, rapot.'
    }

    csv_file = request.FILES.get('file')

    if csv_file is not None:
        if not csv_file.name.endswith('.csv'):
            messages.error(request, "This is not a csv file")

        data_Set = csv_file.read().decode('UTF-8')
        io_string = io.StringIO(data_Set)
        next(io_string)
    
        for column in csv.reader(io_string, delimiter=',', quotechar="|"):
            usr, created = User.objects.get_or_create(
                username = column[0]
            )

            if(created):
                Student.objects.create(user = usr)

            usr.student.nilai1 = column[1]
            usr.student.nilai2 = column[2]
            usr.student.nilai3 = column[3]

            usr.save()
            usr.student.save()

    return render(request, template, context)

def index(request):
    latest_student_list = Student.objects.all()
    template = loader.get_template('polls/index.html')
    context = {
        'latest_student_list': latest_student_list,
    }
    return HttpResponse(template.render(context, request))

def leaderboard(request):
    template = "polls/leaderboard.html"
    return render(request, template)

def login(request):
    template = "polls/login.html"
    return render(request, template)

def nilai(request):
    template = "polls/nilai.html"
    return render(request, template)

def rapot(request):
    template = "polls/rapot.html"
    return render(request, template)

