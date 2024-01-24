from django.views.generic import TemplateView


# 店舗詳細（→ 予約とレビューを会員限定にするにはどうしたらいいのか）
class RestaurantDetailView(TemplateView):
    model = Restaurant
    template_name = "NagoyameshiApp/restaurant_detail.html"
