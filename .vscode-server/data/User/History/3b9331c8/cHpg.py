from django.contrib.auth.views import LoginView


# ログイン
class LoginView(LoginView):
    form_class = AuthenticationForm
    template_name = "NagoyameshiApp/login.html"
