import csv, io
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseForbidden
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ObjectDoesNotExist
from .models import Student
from .forms import CreateUserForm
from django.conf.urls.static import static
from django.db.models import Count
from django.core.paginator import Paginator

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            
            user = form.save()

            s = Student()
            s.user = user
            s.save()

            return redirect('login')


    context = {'form' : form}
    return render(request, 'polls/register.html', context)

def upload(request):
    if not request.user.is_staff:
        return HttpResponseForbidden ("Only for staffs.")

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
                usr.student.xp = column[1]
                usr.student.hp = column[2]
                usr.student.level = column[3]
                usr.student.nilai1 = column[4]
                usr.student.nilai2 = column[5]
                usr.student.nilai3 = column[6]
                usr.student.nilai4 = column[7]
                usr.student.kepemimpinan = column[8]
                usr.student.nasionalisme = column[9]
                usr.student.kebermanfaatan = column[10]
                usr.student.keilmuan = column[11]
                usr.student.adaptif = column[12]
                usr.student.solidaritas = column[13]
                usr.student.kolaboratif = column[14]

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
    current_user = request.user
    user1 = User.objects.get(username='13319002')
    user2 = User.objects.get(username='13319003')
    user3 = User.objects.get(username='13319020')
    context = {
        'user': current_user,
        'user1' : user1,
        'user2' : user2,
        'user3' : user3,
    }
    return render(request, template, context)

def profile(request):
    all_entries = User.objects.order_by('username').filter(is_superuser=False)
    paginator = Paginator(all_entries, 16)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    template = "polls/profile.html"
    context = {
        'page_obj': page_obj,
    }
    
    return render(request, template, context)

def nilai(request):
    if not request.user.is_authenticated:
        return HttpResponseForbidden ("nope.")

    current_user = request.user
    template = "polls/nilai.html"
    context = {
        'user': current_user,
    }    
    return render(request, template, context)

