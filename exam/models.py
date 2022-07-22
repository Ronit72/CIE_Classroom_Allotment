from django.db import models


class Exam(models.Model):
    course_no = models.CharField(db_column='Course_no', primary_key=True, max_length=50)  # Field name made lowercase.
    course_name = models.CharField(db_column='Course_Name', max_length=50, blank=False, null=False)  # Field name made lowercase.
    time_slot = models.TimeField(db_column='Time_slot', blank=False, null=False)  # Field name made lowercase.
    exam_date = models.DateField(db_column='Exam_date', blank=False, null=False)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'exam'