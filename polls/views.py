import csv, io
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.template import loader
from .models import Student
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account was created for ' + user)
            return redirect('login')

    context = {'form' : form}
    return render(request, 'polls/register.html', context)

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
            usr.set_password(column[4])
            usr.first_name = column[5]

            usr.is_active = True
            usr.save()
            usr.student.save()

    return render(request, template, context)



# def registration_view(request):
#     context = {}
#     if request.POST:
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             raw_password = form.cleaned_data.get('password1')
#             account = authenticate(password = password1)
#             login(request, account)
#             return redirect('leaderboard')
#         else:
#             context['registration_form'] = form
#     else:
#         form = RegistrationForm()
#         context['registration_form'] = form
#     return render(request, 'registration/register.html', context)



def leaderboard(request):
    template = "polls/leaderboard.html"
    return render(request, template)

def login(request):
    template = "polls/login.html"
    return render(request, template)

def nilai(request):
    # nilai1 = request.user.student.nilai1
    template = "polls/nilai.html"
    # context = {
    #     'nilai1': nilai1,
    # }    
    return render(request, template)

def rapot(request):
    template = "polls/rapot.html"
    return render(request, template)

