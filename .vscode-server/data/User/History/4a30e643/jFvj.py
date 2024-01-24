from django.views.generic import TemplateView

# **************** 会員（非サブスク会員含む）のみ表示 *****************


# サブスク案内
class SubscriptionGuideView(TemplateView):
    template_name = "NagoyameshiApp/subscription_guide.html"
