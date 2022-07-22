from django.db import models
from django.db.models.aggregates import Max

class Room(models.Model):
    room_no = models.CharField(db_column='Room_no', primary_key=True, max_length=20)  # Field name made lowercase.
    capacity = models.IntegerField(db_column='Capacity', blank=False, null=False)  # Field name made lowercase.
    avaliability_status = models.CharField(db_column='Avaliability_status', max_length=1, blank=False, null=False, default="1")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'room'