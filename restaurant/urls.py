from django.urls import path

from .views import MenuListView, DishDetailView, CategoryListView, CategoryMenuListView

urlpatterns = [
    path('menu/', MenuListView.as_view(), name='menu-list'),
    path('menu/<int:id>/', DishDetailView.as_view(), name='dish_detail'),
    path('menu/categories/', CategoryListView.as_view(), name='category_list'),
    path('menu/categories/<int:category_id>/', CategoryMenuListView.as_view(), name='category_menu_list'),
]
