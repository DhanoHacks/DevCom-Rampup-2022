from django.db import models

# Create your models here.

class Equipment(models.Model):
	name = models.CharField(max_length=200)
	inventory = models.IntegerField()
	available_now = models.IntegerField()

class BorrowedEquipment(models.Model):
	equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
	name = models.CharField(max_length=200)
	returned = models.BooleanField(default=False)