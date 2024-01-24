from django.views.generic import TemplateView


# 店舗一覧
class RestaurantListView(TemplateView):
    model = Restaurant
    template_name = "NagoyameshiApp/restaurant_list.html"
    # context_object_name = ''
    # テンプレートに渡されるオブジェクト名を任意のものに指定できる
    paginate_by = 10
