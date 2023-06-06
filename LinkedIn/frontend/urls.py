from django.contrib import admin
from django.urls import path
from frontend import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home, name="home"),
    path('network/', views.network, name="network"),
    
]
