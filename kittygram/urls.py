from django.urls import path, include
from rest_framework.routers import SimpleRouter

from cats.views import CatViewSet
# from cats.views import CatList, CatDetail
# from cats.views import APICat, APICatDetail
# from cats.views import cat_list, cat_list_detail

# Создаётся роутер
router = SimpleRouter()


# высокоуровневый view-класс
# Вызываем метод .register с нужными параметрами
router.register('cats', CatViewSet)

urlpatterns = [
    # Все зарегистрированные в router пути доступны в router.urls
    # Включим их в головной urls.py
    path('', include(router.urls)),
]


# Дженерики
# urlpatterns = [
#     path('cats/', CatList.as_view()),
#     path('cats/<int:pk>/', CatDetail.as_view()),
# ]


# view-классы низкоуровневые
# urlpatterns = [
#     path('cats/', APICat.as_view()),
#     path('cats/<int:pk>/', APICatDetail.as_view()),
# ]


# view-функции
# urlpatterns = [
#    path('cats/', cat_list),
#    path('cats/<int:pk>/', cat_list_detail),
# ]


