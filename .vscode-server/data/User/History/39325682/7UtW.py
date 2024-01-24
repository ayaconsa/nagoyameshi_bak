from django.views.generic import TemplateView


# 会社概要
class CompanyOverviewView(TemplateView):
    template_name = "NagoyameshiApp/company_overview.html"
