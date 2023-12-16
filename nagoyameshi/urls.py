from django.contrib import admin
from django.urls import path
from NagoyameshiApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.TopView.as_view(), name="top"),
]
