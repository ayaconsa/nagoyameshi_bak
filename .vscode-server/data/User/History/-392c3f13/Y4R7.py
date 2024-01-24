
from django.views.generic import TemplateView

from django.urls import reverse_lazy



# ================== 管理者（サイト運営側）画面 ==================

    



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
    
    


