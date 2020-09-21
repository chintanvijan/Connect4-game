from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    
    path('',views.home,name="home"),
    path('<int:idi>',views.start,name="start"),
    path('<int:idi>/<int:p>',views.update_status,name='update_status'),
]
