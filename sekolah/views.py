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
from .models import KirimPesan
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

    template = "sekolah/nilai.html"
    
    if request.POST.get('accept',""):
        accepted = request.user.accepted_heals.get(id = request.POST.get('heal_id',""))

        if(accepted.valid() and not accepted.read):
            accepted.read = True
            accepted.penerima.student.hp += accepted.heal()
            # sender.student.hp_pot -= heal_int
            # harusnya dikurangi saat ngasih healnya

            accepted.save()
            accepted.penerima.student.save()

    elif request.POST.get('decline',""):
        declined = request.user.accepted_heals.get(id = request.POST.get('heal_id',""))
        
        if(not declined.read):
            declined.read = True
            declined.pengirim.student.hp_pot += declined.potion

            declined.save()
            declined.pengirim.student.save()

    #pesan_masuk = KirimPesan.objects.filter(penerima = current_user, read = False)
    pesan_masuk = request.user.accepted_heals.filter(read = False)

    context = {
        'user': request.user,
        'pesan_masuk' :pesan_masuk,
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
    message = request.POST.get('message', "")

    if not (heal_target == "" or pot_count == "" ) and int(pot_count) > 0:
        target = User.objects.get(username = heal_target)
        
        heal_int = int(pot_count)
        heal_amt = heal_int * 2

        # Error checking
        if heal_int > request.user.student.hp_pot:
            log = format_html("You lack health potions. <br>" + log)
        elif heal_int < 0:
            log = format_html("Don't even think about it. <br>" + log)
        elif target.student.hp + heal_amt > 100:
            log = format_html("You can't heal past maximum health. <br>" + log)  
        elif target.student.alive == False:
            log = format_html("The student you tried to heal is awaiting judgment. <br>" + log)  
        else:
            penerima = User.objects.get(username = heal_target)
            KirimPesan.objects.create(pengirim = request.user, penerima = penerima, potion = pot_count, pesan=message)

            request.user.student.hp_pot -= heal_int
            request.user.student.save()

            log = format_html("Sent heal to " + heal_target + " for " + str(heal_int) + " pots. <br>" + log)

    # Web interfacing, GET logic.
    target_uname = str(request.GET.get('target', ""))
    if target_uname == "":
        target_uname = request.user.username

    try:
        target = User.objects.get(username = target_uname)
    except ObjectDoesNotExist:
        target = request.user
        log = format_html("The user you are trying to heal does not exist.<br>You'll be healing yourself instead.<br>" + log)

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


