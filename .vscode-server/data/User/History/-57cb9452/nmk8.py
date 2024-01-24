from django.views.generic import TemplateView


# トップページ
class TopView(TemplateView):
    template_name = "NagoyameshiApp/top.html"
