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
from .forms import CreateUserForm
from django.conf.urls.static import static
from django.db.models import Count
from django.core.paginator import Paginator
from django.urls import reverse
from django.utils.html import format_html

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
    return render(request, 'sekolah/register.html', context)

def uploadUser(request):
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

def upload(request):
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
                usr.student.hp = int(column[2])
                usr.student.nilai1 = int(column[4])
                usr.student.nilai2 = int(column[5])
                usr.student.nilai3 = int(column[6])
                usr.student.nilai4 = int(column[7])
                usr.student.kepemimpinan = int(column[8])
                usr.student.nasionalisme = int(column[9])
                usr.student.kebermanfaatan = int(column[10])
                usr.student.keilmuan = int(column[11])
                usr.student.adaptif = int(column[12])
                usr.student.solidaritas = int(column[13])
                usr.student.kolaboratif = int(column[14])

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
    template = "sekolah/leaderboard.html"
    current_user = request.user
    usr_list = User.objects.order_by('-student__xp').filter(is_superuser=False)[:10]
    context = {
        'usr_list': usr_list 
    }
    return render(request, template, context)

def mingguan(request):
    template = "sekolah/mingguan.html"
    current_user = request.user
    usr_list = User.objects.order_by('-student__xpminggu').filter(is_superuser=False)[:10]

    xpminggu_bar = []
    for i in range(len(usr_list)):
        xpminggu_bar.append(0)
        xpminggu_bar[i] = usr_list[i].student.xpminggu/usr_list[0].student.xpminggu*100
        
    mylist = zip(usr_list, xpminggu_bar)
    context = {
            'mylist': mylist,
        }
    return render(request, template, context)

def profile(request):
    all_entries = User.objects.order_by('username').filter(is_superuser=False)
    paginator = Paginator(all_entries, 16)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    template = "sekolah/profile.html"
    objek = Angkatan.objects.get(angkatan='Angkatan19')
    context = {
        'page_obj': page_obj,
        'angkatan_xp': objek.xp,
        'angkatan_level': objek.level,
    }
    
    return render(request, template, context)

def nilai(request):
    if not request.user.is_authenticated:
        return HttpResponseForbidden ("nope.")

    current_user = request.user
    template = "sekolah/nilai.html"
    context = {
        'user': current_user,
    }    
    return render(request, template, context)

def landing(request):
    return HttpResponseRedirect(reverse('leaderboard'))

def heal(request):
    target = None
    target_uname = ""
    target_sname = ""
    log = ""

    # Database interfacing, POST logic. Kicks in after submitting when POST data is present.
    heal_target = request.POST.get('target', "")
    pot_count = request.POST.get('count', "")
    if not (heal_target == "" or pot_count == "" ) and int(pot_count) > 0:
        target = User.objects.get(username = heal_target)
        heal_int = int(pot_count)
        heal_amt = heal_int * 2

        # Error checking
        if heal_int > request.user.student.hp_pot:
            log = format_html("You lack health potions. <br>" + log)
        elif target.student.hp + heal_amt > 100:
            log = format_html("You can't heal past maximum health. <br>" + log)  
        else:
            if target.username == request.user.username:
                request.user.student.hp += heal_amt
            else:
                # Somehow doesn't work properly if target is the same as request user
                target.student.hp += heal_amt
                target.student.save()

            request.user.student.hp_pot -= heal_int
            request.user.student.save()

            log = format_html("Healed " + heal_target + " for " + str(heal_int) + " pots.<br>" + log)

    # Web interfacing, GET logic.
    target_uname = str(request.GET.get('target', ""))
    if target_uname == "":
        target_uname = request.user.username

    try:
        target = User.objects.get(username = target_uname)
    except ObjectDoesNotExist:
        target = request.user
        log = format_html("The user you are trying to heal does not exist. <br>")

    if request.user == target:
        target_sname = "yourself"
    else:
        target_sname = target.first_name


    template = "sekolah/heal.html"
    context = {
        'target_sname' : target_sname,
        'user' : request.user,
        'target' : target,
        'log': log
    }
    return render(request, template, context)


