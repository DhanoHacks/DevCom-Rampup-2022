from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Equipment
from .serializers import EquipmentSerializer, BorrowedEquipmentSerializer

@api_view(['GET'])
def getData(response):
	equipments = Equipment.objects.all()
	serializer = EquipmentSerializer(equipments, many=True)
	return Response(serializer.data)

@api_view(['POST'])
def borrowEquipment(request, id):
	equipment = Equipment.objects.get(id=id)
	serializer = BorrowedEquipmentSerializer(data=request.data)
	if serializer.is_valid():
		if(equipment.available_now>0):
			equipment.available_now-=1
			equipment.borrowedequipment_set.create(name=serializer.data['name'])
			equipment.save()
			return Response({"Status":"Success"})
		else:
			return Response({"Status":"Failed: Equipment not available"})
	else:
		return Response({"Status":"Failed: Invalid Format"})

@api_view(['GET'])
def getOneEquipment(response, id):
	output={}
	equipment = Equipment.objects.get(id=id)
	serializer = EquipmentSerializer(equipment, many=False)
	output['equipment']=serializer.data
	borrowed_equipment = equipment.borrowedequipment_set.filter(returned=False)
	serializer = BorrowedEquipmentSerializer(borrowed_equipment, many=True)
	output['current borrowers']=serializer.data
	borrowed_equipment = equipment.borrowedequipment_set.all()
	serializer = BorrowedEquipmentSerializer(borrowed_equipment, many=True)
	output['history']=serializer.data
	return Response(output)

@api_view(['PATCH'])
def returnEquipment(request, id):
	equipment = Equipment.objects.get(id=id)
	currently_borrowed = equipment.borrowedequipment_set.filter(returned=False)
	borrowed_equipment = currently_borrowed.get(name=request.data['name'])
	borrowed_equipment.returned=True
	equipment.available_now+=1
	borrowed_equipment.save()
	equipment.save()
	serializer = BorrowedEquipmentSerializer(borrowed_equipment, many=False)
	return Response(serializer.data)