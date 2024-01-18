from django.contrib import admin
from django.urls import path
from NagoyameshiApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('', views.TopView.as_view(), name="top"),
    path('company_overview/', views.CompanyOverviewView.as_view(), name="company_overview"),
    path('terms_of_use/', views.TermsOfUseView.as_view(), name="terms_of_use"),

    path('account_create/', views.CreateAccountView.as_view(), name="account_create"),
    path('login/', views.LoginView.as_view(), name="login"),   
    path('restaurant_list/', views.RestaurantListView.as_view(), name="restaurant_list"),
    path('restaurant_detail/', views.RestaurantDetailView.as_view(), name="restaurant_detail"),

    path('logout/', views.LogoutView.as_view(), name="logout"),
    path('password_resetting/', views.PasswordResettingView.as_view(), name="password_resetting"),
    path('subscription_guide/', views.SubscriptionGuideView.as_view(), name="subscription_guide"),
    path('delete_account/', views.DeleteAccountView.as_view(), name="delete_account"),

    path('account_info', views.AccountInfoView.as_view(), name="account_info"),
    path('bookings', views.BookingsView.as_view(), name="bookings"),
    path('favorites', views.FavoritesView.as_view(), name="favorites"),
    path('change_payment_method', views.ChangePaymentMethodView.as_view(), name="change_payment_method"),
    path('unsubscribe', views.UnsubscribeView.as_view(), name="unsubscribe"),
    
    
    
    path('manage/', views.ManageTopView.as_view(), name="manage_top"),
    path('manage/login', views.ManageLoginView.as_view(), name="manage_login"),
    path('manage/restaurant_info', views.RestaurantInfoView.as_view(), name="manage_restaurant_info"),
    path('manage/booking_confirmation', views.BookingConfirmationView.as_view(), name="manage_booking_confirmation"),
    path('manage/review_confirmation', views.ReviewConfirmationView.as_view(), name="manage_review_confirmation"),
    
    
    
    path('admin/', admin.site.urls),
    path('admin/login', views.AdminLoginView.as_view(), name="admin_login"),
    path('admin/top', views.AdminTopView.as_view(), name="admin_top"),
    path('admin/category_list', views.CategoryListView.as_view(), name="admin_category_list"),
    path('admin/user_list', views.UserListView.as_view(), name="admin_user_list"),
    path('admin/sales', views.SalesView.as_view(), name="admin_sales"),
    path('admin/user_number', views.UserNumberView.as_view(), name="admin_user_number"),
    
]
