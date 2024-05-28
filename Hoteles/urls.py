from django.contrib import admin
from django.urls import path
from Reservaciones import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('contacto/', views.contacto, name= 'contacto'),
    path('reservacion/', views.crear_reservacion, name='reservacion'),
]