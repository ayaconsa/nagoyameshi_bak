from django.contrib import admin
from django.urls import path
from NagoyameshiApp import views_org
from django.conf import settings
from django.conf.urls.static import static

from NagoyameshiApp.views.user.top_view import TopView

urlpatterns = [
    
    path('', views_org.TopView.as_view(), name="top"),
    path('company_overview/', views_org.CompanyOverviewView.as_view(), name="company_overview"),
    path('terms_of_use/', views_org.TermsOfUseView.as_view(), name="terms_of_use"),

    path('account_create/', views_org.CreateAccountView.as_view(), name="account_create"),
    path('login/', views_org.LoginView.as_view(), name="login"),   
    path('restaurant_list/', views_org.RestaurantListView.as_view(), name="restaurant_list"),
    path('restaurant_detail/', views_org.RestaurantDetailView.as_view(), name="restaurant_detail"),

    path('logout/', views_org.LogoutView.as_view(), name="logout"),
    path('password_resetting/', views_org.PasswordResettingView.as_view(), name="password_resetting"),
    path('subscription_guide/', views_org.SubscriptionGuideView.as_view(), name="subscription_guide"),
    path('delete_account/', views_org.DeleteAccountView.as_view(), name="delete_account"),

    path('account_info', views_org.AccountInfoView.as_view(), name="account_info"),
    path('bookings', views_org.BookingsView.as_view(), name="bookings"),
    path('favorites', views_org.FavoritesView.as_view(), name="favorites"),
    path('change_payment_method', views_org.ChangePaymentMethodView.as_view(), name="change_payment_method"),
    path('unsubscribe', views_org.UnsubscribeView.as_view(), name="unsubscribe"),
    
    
    
    path('manage/', views_org.ManageTopView.as_view(), name="manage_top"),
    path('manage/login', views_org.ManageLoginView.as_view(), name="manage_login"),
    path('manage/restaurant_info', views_org.RestaurantInfoView.as_view(), name="manage_restaurant_info"),
    path('manage/booking_confirmation', views_org.BookingConfirmationView.as_view(), name="manage_booking_confirmation"),
    path('manage/review_confirmation', views_org.ReviewConfirmationView.as_view(), name="manage_review_confirmation"),
    
    
    
    path('admin/', admin.site.urls),
    path('admin/login', views_org.AdminLoginView.as_view(), name="admin_login"),
    path('admin/top', views_org.AdminTopView.as_view(), name="admin_top"),
    path('admin/category_list', views_org.CategoryListView.as_view(), name="admin_category_list"),
    path('admin/user_list', views_org.UserListView.as_view(), name="admin_user_list"),
    path('admin/sales', views_org.SalesView.as_view(), name="admin_sales"),
    path('admin/user_number', views_org.UserNumberView.as_view(), name="admin_user_number"),
    
]
