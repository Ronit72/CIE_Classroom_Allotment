from django.db import models

# Create your models here.
class Excel(models.Model):
    title = models.CharField(max_length=100)
    xls = models.FileField(upload_to="excel")

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.xls.delete()
        super().delete( *args, **kwargs)

class Schedule(models.Model):
    title = models.CharField(max_length=100)
    pdf = models.FileField(upload_to="schedule")

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        super().delete( *args, **kwargs)

