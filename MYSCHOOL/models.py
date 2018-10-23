from django.db import models
from django.utils import timezone
# Create your models here.

class TblStudent(models.Model):
    sid = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=500, blank=True, null=True)
    nick_name = models.CharField(max_length=50, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(default=timezone.now)
    create_by = models.ForeignKey('auth.User',default='1', on_delete=models.CASCADE)


    def publish(self):
        self.create_date = timezone.now()
        self.create_by = '1'
        self.save()

    def __str__(self):
        return self.full_name