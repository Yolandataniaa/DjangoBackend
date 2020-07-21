from django.urls import reverse
from django.utils.html import format_html
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect

from django.contrib import admin
from .models import Student
from .models import Task
from .models import Angkatan

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'net_stat', 'hp_pot', 'link_to_tasks')

    def link_to_tasks(self, obj):
        tasks = obj.task_set.all().order_by('week', 'detail')
        link = ""

        #link = reverse("admin:index", args=[obj.id])
        for task in tasks:
            edit_link = reverse("admin:sekolah_task_change", args=[task.id])
            link += format_html('<a href="{}">{}_w{}({})</a>, ', edit_link, task.detail, task.week, task.score)

        #return format_html('<a href="{}">Edit {}</a>', link, obj.Task.detail)
        return format_html(link)
    
    link_to_tasks.short_description = 'Edit task score'

class TaskAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'score')

    def response_change(self, request, obj, post_url_continue=None):
        return HttpResponseRedirect(reverse("admin:sekolah_student_changelist"))


admin.site.register(Task, TaskAdmin)
admin.site.register(Student, StudentAdmin)
