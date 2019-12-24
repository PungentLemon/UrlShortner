from django.contrib import admin
from django.urls import path
from mainapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<str:token>', views.home, name='home'),
    path('',views.make, name= 'Make new'),
]
