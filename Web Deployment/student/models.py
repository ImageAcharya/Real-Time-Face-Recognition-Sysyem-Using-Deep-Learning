from django.db import models
import datetime

# Create your models here.

class Student(models.Model):
    id = models.CharField(max_length = 100, primary_key=True)
    fname = models.CharField(max_length = 100)
    lname = models.CharField(max_length = 100)

    def __str__(self):
        return self.fname+' '+self.lname+' ('+self.id+')'

class Attendance(models.Model):
    faculty = models.CharField(max_length=100, null=True)
    semester = models.CharField(max_length=100, null=True)
    section = models.CharField(max_length=100, null = True)
    studentid = models.ForeignKey(Student, blank=True, null=True, on_delete=models.CASCADE)
    datentime = models.DateTimeField(default = datetime.datetime.now())
    
    def __str__(self):
        return self.studentid.fname+' '+self.studentid.lname+' ('+self.studentid.id+')'

