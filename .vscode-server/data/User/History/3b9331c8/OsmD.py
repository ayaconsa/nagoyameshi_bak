from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm


# ログイン
class UserLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = "NagoyameshiApp/login.html"
