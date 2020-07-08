from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Student(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)

    nilai1 = models.IntegerField(default=0)
    nilai2 = models.IntegerField(default=0)
    nilai3 = models.IntegerField(default=0)
    nilai4 = models.IntegerField(default=0)
    kepemimpinan = models.IntegerField(default=0)
    nasionalisme = models.IntegerField(default=0)
    kebermanfaatan = models.IntegerField(default=0)
    keilmuan  = models.IntegerField(default=0)
    adaptif = models.IntegerField(default=0)
    solidaritas = models.IntegerField(default=0)
    kolaboratif = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

# class NilaiMinggu1(models.Model):
#     student = models.OneToOneField(Student, on_delete = models.CASCADE)

#     nilai1 = models.IntegerField(null=True, default=0)

#     def __str__(self):
#         return self.student.name

# class NilaiMinggu2(models.Model):
#     student = models.OneToOneField(Student, on_delete = models.CASCADE)

#     nilai2 = models.IntegerField(default=0)

#     def __str__(self):
#         return self.student.name

# class NilaiMinggu3(models.Model):
#     student = models.OneToOneField(Student, on_delete = models.CASCADE)

#     nilai3 = models.IntegerField(default=0)

#     def __str__(self):
#         return self.student.name

# class Rapot(models.Model):
#     student = models.OneToOneField(Student, on_delete = models.CASCADE)

#     keaktifan = models.CharField(max_length=2, default="")
#     pemahamanMateri = models.CharField(max_length=2, default="")
#     kedisiplinan = models.CharField(max_length=2, default="")
    
#     def __str__(self):
#         return self.student.name      