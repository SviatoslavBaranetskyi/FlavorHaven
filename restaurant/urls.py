from django.urls import path

from .views import MenuListView, DishDetailView, CategoryListView, CategoryMenuListView, ReservationListView

urlpatterns = [
    path('menu', MenuListView.as_view(), name='menu-list'),
    path('menu/<int:id>', DishDetailView.as_view(), name='dish_detail'),
    path('categories', CategoryListView.as_view(), name='category_list'),
    path('categories/<int:category_id>/dishes', CategoryMenuListView.as_view(), name='category_menu_list'),
    path('reservations', ReservationListView.as_view(), name='reservation-list')
]
