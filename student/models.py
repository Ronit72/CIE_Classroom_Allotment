from typing import Pattern
from django.db import models

class Student(models.Model):
    usn = models.CharField(db_column='USN', primary_key=True, max_length=50)  # Field name made lowercase.
    semester = models.CharField(db_column='Semester', max_length=10, blank=False, null=False)  # Field name made lowercase.
    department = models.CharField(db_column='Department', max_length=100, blank=False, null=False)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=False, null=False)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'student'
