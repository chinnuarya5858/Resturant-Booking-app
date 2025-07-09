from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Table(models.Model):
    table_number=models.IntegerField(unique=True)
    capacity=models.IntegerField()
    STATUS_CHOICES=[('available','Available'),('reserved','Reserved')]
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='available')
    def __str__(self):
        return str(self.table_number)



class Booking(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=False)
    table=models.ForeignKey(Table,on_delete=models.CASCADE,null=True, blank=False)
    booking_time=models.DateTimeField()
    status=models.CharField(max_length=20,default='pending')

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        if self.table:
            self.table.status='reserved'
            self.table.save()

    def __str__(self):
        return f"Booking by {self.user.username} at {self.booking_time}"

    
class Menu(models.Model):
    name=models.CharField(max_length=200)
    price=models.IntegerField(null=False)
    menu_item_description=models.TextField(max_length=1000,default='')

    def __str__(self):
        return self.name