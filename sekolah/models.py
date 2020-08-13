from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Student(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)

    xp = models.IntegerField(default=0)
    xpminggu  = models.IntegerField(default=0)
    hp = models.IntegerField(default=100)
    level = models.CharField(max_length=20, default="Sailors")
    hp_pot = models.IntegerField(default=0)
    alive = models.BooleanField(default=True)
    jumlahpotion = models.IntegerField(default=0)

    kepemimpinan = models.IntegerField(default=0)
    nasionalisme = models.IntegerField(default=0)
    kebermanfaatan = models.IntegerField(default=0)
    keilmuan  = models.IntegerField(default=0)
    adaptif = models.IntegerField(default=0)
    solidaritas = models.IntegerField(default=0)
    kolaboratif = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

    milestones = [
        0,
        1000,
        3800,
        9000,
        17000,
        28800,
        100000
    ]

    rank =[
        "Sailors",
        "Gunners",
        "Boatswain",
        "Lieutenants",
        "Sailing Master",
        "First Mate",
    ]

    def xp_current(self):
        for i in range(len(self.rank)):
            if self.level == self.rank[i]:
                low = self.milestones[i]
                return self.xp - low

    def xp_bar(self):
        for i in range(len(self.rank)):
            if self.level == self.rank[i]:
                low = self.milestones[i]
                high = self.milestones[i+1]
                diff = high - low
                return (100.0 * (self.xp-low))/diff

    def net_stat(self):
        net = self.kepemimpinan + self.nasionalisme + self.kebermanfaatan + self.keilmuan + self.adaptif + self.solidaritas + self.kolaboratif
        return net

    def tasks_ordered(self):
        return self.task_set.all().order_by('week', 'detail')

    def save(self, *args, **kwargs):
        for i in range(len(self.milestones)):
            if self.milestones[i] <= self.xp and self.xp < self.milestones[i+1]:
                self.level = self.rank[i]

        if self.hp <=0:
            self.hp = 0
            self.alive = False
        elif self.hp > 0:
            self.alive = True

        super(Student, self).save(*args, **kwargs)

    

class Task(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    detail = models.CharField(max_length=40, default="")
    week = models.IntegerField(default=0)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.student.user.first_name + "'s week " + str(self.week) + " " + self.detail + " score"


class Angkatan(models.Model):
    angkatan = models.CharField(max_length=20, default="")
    xp = models.IntegerField(default=100)
    level = models.CharField(max_length=20, default="Sailors")

    def __str__(self):
        return self.angkatan

    milestones = [
        0,
        1000,
        2000,
        3000,
        4000,
        10000
    ]

    rank =[
        "Corsario",
        "Bucanero",
        "Filibustero",
        "Engage",
    ]

    def xp_current(self):
        for i in range(len(self.rank)):
            if self.level == self.rank[i]:
                low = self.milestones[i]
                return self.xp - low

    def xp_bar(self):
        for i in range(len(self.rank)):
            if self.level == self.rank[i]:
                low = self.milestones[i]
                high = self.milestones[i+1]
                diff = high - low
                return (100.0 * (self.xp-low))/diff

    def save(self, *args, **kwargs):
        for i in range(len(self.milestones)):
            if self.milestones[i] <= self.xp and self.xp < self.milestones[i+1]:
                self.level = self.rank[i]

        super(Angkatan, self).save(*args, **kwargs)

class KirimPesan(models.Model):
    pengirim = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pengirim', null=True)
    penerima = models.ForeignKey(User, on_delete=models.CASCADE, related_name='penerima', null=True)

    potion = models.IntegerField(default=0)
    pesan = models.CharField(max_length=40, default="Tidak ada pesan")
    read = models.BooleanField(default=False)

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
