from django.urls import path
from . import views

urlpatterns = [
	path('get',views.getData),
	path('<int:id>',views.getOneEquipment),
	path('<int:id>/borrow',views.borrowEquipment),
	path('<int:id>/return',views.returnEquipment)
	
]