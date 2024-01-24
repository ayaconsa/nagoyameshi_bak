from django.shortcuts import render, redirect

from django.views.generic import TemplateView

from django.urls import reverse_lazy

from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

from .models import Restaurant




# **************** 会員（非サブスク会員含む）のみ表示 *****************




# サブスク案内
class SubscriptionGuideView(TemplateView):
    template_name = "NagoyameshiApp/subscription_guide.html"
    

# アカウント削除
class DeleteAccountView(TemplateView):
    template_name = "NagoyameshiApp/delete_account.html"


# **************** サブスク会員のみ表示 *****************

# 会員情報
class AccountInfoView(LoginRequiredMixin, TemplateView):
    model = User
    template_name = "NagoyameshiApp/acount_info.html"


# 予約一覧
class BookingsView(TemplateView):
    template_name = "NagoyameshiApp/bookings.html"


# お気に入り一覧
class FavoritesView(TemplateView):
    template_name = "NagoyameshiApp/favorites.html"


# お支払い方法変更
class ChangePaymentMethodView(TemplateView):
    template_name = "NagoyameshiApp/change_payment_method.html"


# サブスク解約
class UnsubscribeView(TemplateView):
    template_name = "NagoyameshiApp/unsubscribe.html"



# ================== 管理（店舗側）画面 ==================

# 管理者（店舗）ログイン
class ManageLoginView(TemplateView):
    template_name = "NagoyameshiApp/manage/manage_login.html"
    

# 管理者（店舗）トップページ
class ManageTopView(TemplateView):
    template_name = "NagoyameshiApp/manage/manage_top.html"


# 店舗情報（登録・編集・削除）
class RestaurantInfoView(LoginRequiredMixin, TemplateView):
    model = Restaurant
    fields = '__all__' #フィールド内全件指定
    # fields = ["title", "image", "text"]のように指定することも可
    template_name = "NagoyameshiApp/manage/restaurant_info.html"
    

# 予約確認
class BookingConfirmationView(TemplateView):
    template_name = "NagoyameshiApp/manage/booking_confirmation.html"
    

# レビュー確認
class ReviewConfirmationView(TemplateView):
    template_name = "NagoyameshiApp/manage/review_confirmation.html"
    


# ================== 管理者（サイト運営側）画面 ==================

# 管理者（サイト運営者）ログイン
class AdminLoginView(TemplateView):
    template_name = "NagoyameshiApp/admin/admin_login.html"
    

# 管理者（サイト運営者）トップページ
class AdminTopView(TemplateView):
    template_name = "NagoyameshiApp/admin/admin_top.html"


# カテゴリ管理
class CategoryListView(TemplateView):
    template_name = "NagoyameshiApp/admin/category_list.html"


# 会員一覧
class UserListView(TemplateView):
    template_name = "NagoyameshiApp/admin/user_list.html"


# 売り上げ集計ページ
class SalesView(TemplateView):
    template_name = "NagoyameshiApp/admin/sales.html"
    
    
# 会員数集計ページ
class UserNumberView(TemplateView):
    template_name = "NagoyameshiApp/admin/user_number.html"
    
    


