from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200, null = True, default="")
    nilai1 = models.IntegerField(default=0)
    nilai2 = models.IntegerField(default=0)
    nilai3 = models.IntegerField(default=0)
    rank = models.CharField(max_length=2, default="")

    def __str__(self):
        return self.name

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