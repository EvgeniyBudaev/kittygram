from django.urls import path

from cats.views import cat_list, cat_list_detail

urlpatterns = [
   path('cats/', cat_list),
   path('cats/<int:pk>/', cat_list_detail),
]


