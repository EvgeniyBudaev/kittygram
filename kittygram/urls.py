from django.urls import path

# from cats.views import CatList, CatDetail
from cats.views import APICat, APICatDetail
# from cats.views import cat_list, cat_list_detail


# urlpatterns = [
#     path('cats/', CatList.as_view()),
#     path('cats/<int:pk>/', CatDetail.as_view()),
# ]


# view-классы низкоуровневые
urlpatterns = [
    path('cats/', APICat.as_view()),
    path('cats/<int:pk>/', APICatDetail.as_view()),
]


# view-функции
# urlpatterns = [
#    path('cats/', cat_list),
#    path('cats/<int:pk>/', cat_list_detail),
# ]


