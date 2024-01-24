from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView



# パスワード再設定ページ
class PasswordResettingView(LoginRequiredMixin, TemplateView):
    template_name = "NagoyameshiApp/password_resetting.html"
