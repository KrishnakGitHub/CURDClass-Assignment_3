from django.db import models

# Create your models here.
DEPT_CHOICES = [
    ('CSE','CSE'),
    ('ME','ME'),
    ('CIVIL','CIVIL'),
    ('EE','EE'),
]

class Student(models.Model):
	Student_Name = models.CharField(max_length=100)
	Roll_Number = models.PositiveIntegerField()
	Year_Of_Joining = models.PositiveIntegerField()
	Course = models.CharField(max_length=100,choices=DEPT_CHOICES)
	cr_date = models.DateTimeField(auto_now_add=True)