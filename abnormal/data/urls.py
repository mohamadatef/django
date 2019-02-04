from django.urls import  path
from . import views



urlpatterns = [

    path ('' , views.index , name = 'index'), 
    path ('<int:x>/', views.sample , name = 'detail'), 
    path ('add/' , views.addData, name  = 'addData'),
    path ('edit/<int:id>/' , views.editData, name  = 'editData')



]