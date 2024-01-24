from django.shortcuts import render, redirect

from django.views.generic import TemplateView

from django.urls import reverse_lazy

from django.contrib.auth import login, authenticate




# ================== 管理（店舗側）画面 ==================

    



    

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
    
    


