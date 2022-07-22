from django.db import models

class Invigilator(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=50)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=255, blank=False, null=False)  # Field name made lowercase.
    invigilation_count = models.IntegerField(db_column='Invigilation_count', blank=True, null=False)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, blank=False, null=False)  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'invigilator'
