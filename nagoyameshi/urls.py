from django.contrib import admin
from django.urls import path
from NagoyameshiApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.TopView.as_view(), name="top"),
    path('company_overview/', views.CompanyOverviewView.as_view(), name="company_overview"),
    path('terms_of_use/', views.TermsOfUseView.as_view(), name="terms_of_use"),
    path('login/', views.LoginView.as_view(), name="login"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
    path('create/', views.CreateAccountView.as_view(), name="create"),
    path('list/', views.RestaurantListView.as_view(), name="list"),
    path('detail/', views.RestaurantDetailView.as_view(), name="detail"),
    path('detail/', views.RestaurantDeleteView.as_view(), name="delete"),
    
]
