from django.db import models
from invigilator.models import Invigilator

class Timetable(models.Model):
    on_date = models.DateField()  # Field name made lowercase.
    free_time = models.TimeField()  # Field name made lowercase.
    invigilator = models.ForeignKey(Invigilator, on_delete=models.CASCADE, related_name='timetables')

    class Meta:
        managed = False
        db_table = 'timetable'