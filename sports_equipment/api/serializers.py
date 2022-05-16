from rest_framework import serializers
from base.models import Equipment, BorrowedEquipment

class EquipmentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Equipment
		fields = '__all__'

class BorrowedEquipmentSerializer(serializers.ModelSerializer):
	class Meta:
		model = BorrowedEquipment
		fields = ('id','name','returned')