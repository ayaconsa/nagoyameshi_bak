from django.shortcuts import render, redirect

from django.views.generic import TemplateView
from django.views.generic.list import ListView, BaseListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from .models import Restaurant
from .forms import UserCreateForm


# **********トップページ・会社概要・利用規約**********

class TopView(TemplateView):
    template_name = "NagoyameshiApp/top.html"

class CompanyOverviewView(TemplateView):
    template_name = "NagoyameshiApp/company_overview.html"

class TermsOfUseView(TemplateView):
    template_name = "NagoyameshiApp/terms_of_use.html"

# *********認証機能*************

class CreateAccountView(CreateView):
    def post(self, request, *args, **kwargs):
        form = UserCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            #フォームから'username'を読み取る
            username = form.cleaned_data.get("username")
            #フォームから'password1'を読み取る
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("/")
        return render(request, "NagoyameshiApp/reate.html", {"form": form,})

    def get(self, request, *args, **kwargs):
        form = UserCreateForm(request.POST)
        return  render(request, "NagoyameshiApp/create.html", {"form": form,})

create_account = CreateAccountView.as_view()


class LoginView(LoginView):
    form_class = AuthenticationForm
    template_name = "NagoyameshiApp/login.heml"

# 継承の順番重要
# LoginRequiredMixinはログイン状態でのみ表示されるview → 非ログイン時はログイン画面に遷移
class LogoutView(LoginRequiredMixin, LogoutView):
    template_name = "NagoyameshiApp/logout.heml"


# *********店舗機能****************
    

# ユーザー画面では、TemplateViewにしてしまうことも多い
class RestaurantListView(TemplateView):
    model = Restaurant
    template_name = "NagoyameshiApp/list.html"
    # context_object_name = ''
    # テンプレートに渡されるオブジェクト名を任意のものに指定できる
    paginate_by = 10
    
# ユーザー画面では、TemplateViewにしてしまうことも多い
class RestaurantDetailView(TemplateView):
    model = Restaurant
    template_name = "NagoyameshiApp/detail.html"
    
    

class RestaurantCreateView(LoginRequiredMixin, CreateView):
    model = Restaurant
    fields = '__all__' #フィールド内全件指定
    # fields = ["title", "image", "text"]のように指定することも可

class RestaurantUpdateView(LoginRequiredMixin, UpdateView):
    model = Restaurant
    fields = '__all__'

class RestaurantDeleteView(LoginRequiredMixin, DeleteView):
    model = Restaurant
    template_name = "Nagoyameshi/detail.html"
    success_url = reverse_lazy('list')
    
    

# *********管理用画面*********

class ManageTopView(TemplateView):
    template_name = "Nagoyameshi/manage_top.html"