from . import views
from django.urls import path

urlpatterns=[
	path('to_do/',views.index, name="index"),
	path('to_do/<str:pk>/update',views.updateTask, name="update_task"),
	path('to_do/<str:pk>/delete',views.deleteTask, name="delete_task"),

	path('',views.index, name="index")

]