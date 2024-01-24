
from django.views.generic import TemplateView

# from django.urls import reverse_lazy



# ================== 管理者（サイト運営側）画面 ==================

    
    
# 会員数集計ページ
class UserNumberView(TemplateView):
    template_name = "NagoyameshiApp/admin/user_number.html"
    
    


