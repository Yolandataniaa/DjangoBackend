import csv, io
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ObjectDoesNotExist
from .models import Student
from .models import Angkatan
from .models import Task
from .forms import CreateUserForm
from django.conf.urls.static import static
from django.db.models import Count
from django.core.paginator import Paginator
from django.urls import reverse
from django.utils.html import format_html

def upload_user(request):
    if not request.user.is_staff:
        return HttpResponseForbidden ("Only for staffs.")

    csv_file = request.FILES.get('file')
    unsaved = 0
    unsaved_str = ""
    template = "sekolah/uploadUser.html"

    if csv_file is not None:
        if not csv_file.name.endswith('.csv'):
            messages.error(request, "This is not a csv file")

        data_Set = csv_file.read().decode('UTF-8')
        io_string = io.StringIO(data_Set)
        next(io_string)
    
        for column in csv.reader(io_string, delimiter=',', quotechar="|"):
            try:
                usr = User.objects.get(username=column[0])
            except ObjectDoesNotExist:
                usr = User(username=column[0])
            
            usr.first_name=column[1]
            usr.last_name=column[2]
            usr.is_active = True
            usr.save()

            student = Student()
            student.user = usr
            student.save()

    if unsaved > 0 :
        unsaved_str = "There are " + str(unsaved) + " unsaved data from previous upload"

    context = {
        'order' : 'Order of CSV should be nim, first_name, last_name',
        'unsaved' : unsaved_str
    }

    return render(request, template, context)

def upload_stat(request):
    if not request.user.is_staff:
        return HttpResponseForbidden ("Only for staffs.")

    csv_file = request.FILES.get('file')
    unsaved = 0
    unsaved_str = ""
    template = "sekolah/upload.html"

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
                usr.student.xp = int(column[1])
                usr.student.xpminggu = int(column[2])
                usr.student.kepemimpinan = int(column[3])
                usr.student.nasionalisme = int(column[4])
                usr.student.kebermanfaatan = int(column[5])
                usr.student.keilmuan = int(column[6])
                usr.student.adaptif = int(column[7])
                usr.student.solidaritas = int(column[8])
                usr.student.kolaboratif = int(column[9])

                usr.is_active = True
                usr.save()
                usr.student.save()

            else:
                unsaved = unsaved + 1

    if unsaved > 0 :
        unsaved_str = "There are " + str(unsaved) + " unsaved data from previous upload"

    context = {
        'order' : 'Order of CSV should be nim, xp, xpminggu, kepemimpinan, nasionalisme, kebermanfaatan, keilmuan, adaptif, solidaritas, kolaboratif.',
        'unsaved' : unsaved_str
    }

    return render(request, template, context)

def upload_marks(request):
    if not request.user.is_staff:
        return HttpResponseForbidden ("Only for staffs.")

    csv_file = request.FILES.get('file')
    unsaved = 0
    unsaved_str = ""
    template = "sekolah/upload.html"

    if csv_file is not None:
        if not csv_file.name.endswith('.csv'):
            messages.error(request, "This is not a csv file")

        data_Set = csv_file.read().decode('UTF-8')
        io_string = io.StringIO(data_Set)
        
        # Parse first line to identify uploaded marks
        detail_list = next(csv.reader(io_string))

        # Parse individual marks
        for column in csv.reader(io_string, delimiter=',', quotechar="|"):
            try:
                usr = User.objects.get(username = column[0])
            except ObjectDoesNotExist:
                usr = None
            
            if usr is not None:
                for i in range(1, len(detail_list), 2):
                    try:
                        task = Task.objects.get(
                            student=usr.student, 
                            detail=detail_list[i],
                            week=detail_list[i+1])
                    except ObjectDoesNotExist:
                        task = Task(
                            student=usr.student, 
                            detail=detail_list[i],
                            week=detail_list[i+1])
                    
                    task.score = int(column[i])
                    task.save()

            else:
                unsaved = unsaved + 1

    if unsaved > 0 :
        unsaved_str = "There are " + str(unsaved) + " unsaved data from previous upload"

    context = {
        'order' : 'Order of CSV should be nim, <task 1s score>, <task 1s week>, <task 2s score>, <task 2s week>, etc..',
        'unsaved' : unsaved_str
    }

    return render(request, template, context)

def upload_damage(request):
    if not request.user.is_staff:
        return HttpResponseForbidden ("Only for staffs.")

    csv_file = request.FILES.get('file')
    unsaved = 0
    unsaved_str = ""
    template = "sekolah/upload.html"

    if csv_file is not None:
        if not csv_file.name.endswith('.csv'):
            messages.error(request, "This is not a csv file")

        data_Set = csv_file.read().decode('UTF-8')
        io_string = io.StringIO(data_Set)
        
        # Parse first line to identify uploaded marks
        detail_list = next(csv.reader(io_string))

        # Parse individual marks
        for column in csv.reader(io_string, delimiter=',', quotechar="|"):
            try:
                usr = User.objects.get(username = column[0])
            except ObjectDoesNotExist:
                usr = None
            
            if usr is not None:
                usr.student.hp -= int(column[1])

                usr.is_active = True
                usr.save()
                usr.student.save()

            else:
                unsaved = unsaved + 1

    if unsaved > 0 :
        unsaved_str = "There are " + str(unsaved) + " unsaved data from previous upload"

    context = {
        'order' : format_html('For mass-damaging.<br>Order of CSV should be nim, damage.'),
        'unsaved' : unsaved_str
    }

    return render(request, template, context)

def upload_potions(request):
    if not request.user.is_staff:
        return HttpResponseForbidden ("Only for staffs.")

    csv_file = request.FILES.get('file')
    unsaved = 0
    unsaved_str = ""
    template = "sekolah/upload.html"

    if csv_file is not None:
        if not csv_file.name.endswith('.csv'):
            messages.error(request, "This is not a csv file")

        data_Set = csv_file.read().decode('UTF-8')
        io_string = io.StringIO(data_Set)
        
        # Parse first line to identify uploaded marks
        detail_list = next(csv.reader(io_string))

        # Parse individual marks
        for column in csv.reader(io_string, delimiter=',', quotechar="|"):
            try:
                usr = User.objects.get(username = column[0])
            except ObjectDoesNotExist:
                usr = None
            
            if usr is not None:
                usr.student.hp_pot += int(column[1])

                usr.is_active = True
                usr.save()
                usr.student.save()

            else:
                unsaved = unsaved + 1

    if unsaved > 0 :
        unsaved_str = "There are " + str(unsaved) + " unsaved data from previous upload"

    context = {
        'order' : format_html('For mass potion distribution.<br>Order of CSV should be nim, extra_pot.'),
        'unsaved' : unsaved_str
    }

    return render(request, template, context)