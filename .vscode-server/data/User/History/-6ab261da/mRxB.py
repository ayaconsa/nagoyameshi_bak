from django.views.generic import TemplateView


# 利用規約
class TermsOfUseView(TemplateView):
    template_name = "NagoyameshiApp/terms_of_use.html"
