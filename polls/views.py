import csv, io
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from django.template import loader
from .models import Student
# from .models import NilaiMinggu1
# from .models import NilaiMinggu2
# from .models import NilaiMinggu3

# Create your views here.

def upload(request):

    template = "polls/upload.html"

    prompt = {
        'order' : 'Order of CSV should be name, nilaiminggu1, nilaiminggu2, nilaiminggu3, rapot'
    }

    if request.method =="GET":
        return render(request, template, prompt)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, "This is not a csv file")

    data_Set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_Set)
    next(io_string)

    #     s = Student.objects.create()
    # nm1 =  NilaiMinggu1.objects.create(nilai1 = 0)
    # s.nilaiminggu1 = nm1

    # nm1.save()
    # s.save()
    
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Student.objects.update_or_create(
            name = column[0],
            nilai1 = column[1],
            nilai2 = column[2],
            nilai3 = column[3],
            rank = column[4]
        )   
    
        #     _, created = Student.objects.update_or_create(
        #     name = column[0]
        # )   
        # _, created = NilaiMinggu1.objects.update_or_create(
        #     nilai1 = column[1]
        # ) 
        # _, created = NilaiMinggu2.objects.update_or_create(
        #     nilai2 = column[2]
        # )                 
        # _, created = NilaiMinggu3.objects.update_or_create(
        #     nilai3 = column[3]
        # )   

    context = {}
    return render(request, template, context)

def index(request):
    latest_student_list = Student.objects.all()
    template = loader.get_template('polls/index.html')
    context = {
        'latest_student_list': latest_student_list,
    }
    return HttpResponse(template.render(context, request))

def home(request):
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
