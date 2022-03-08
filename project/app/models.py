# from pyexpat import model
# from statistics import mode
from django.db import models

# Create your models here.
class Student(models.Model):
    sname = models.CharField(max_length=20)
    srno = models.IntegerField()
    ssec = models.CharField(max_length=4)
    scourse = models.CharField(max_length=10)
    def __str__(self):
        return self.sname