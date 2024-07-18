from django.db import models


class Course(models.Model):
    course_code = models.CharField(max_length=100)
    course_name = models.CharField(max_length=100)
    course_credits = models.IntegerField()

class student(models.Model):
    usn = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    sem = models.IntegerField()
    enrollment = models.ManyToManyField(Course) 

