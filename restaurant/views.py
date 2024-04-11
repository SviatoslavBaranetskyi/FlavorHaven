from django.utils import timezone
from rest_framework import generics
from drf_yasg.utils import swagger_auto_schema

from .models import Menu, Category, Reservation
from .serializers import MenuSerializer, CategorySerializer, ReservationSerializer


class MenuListView(generics.ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    @swagger_auto_schema(operation_summary="Get list of all menus")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class DishDetailView(generics.RetrieveAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    lookup_field = 'id'

    @swagger_auto_schema(operation_summary="Get details of a dish by ID")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @swagger_auto_schema(operation_summary="Get list of all categories")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class CategoryMenuListView(generics.ListAPIView):
    serializer_class = MenuSerializer

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return Menu.objects.filter(categories__id=category_id)

    @swagger_auto_schema(operation_summary="Get list of dishes by category ID")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class ReservationListView(generics.ListCreateAPIView):
    serializer_class = ReservationSerializer

    def get_queryset(self):
        # Удаляем прошлые бронирования перед выполнением запроса
        past_reservations = Reservation.objects.filter(date__lt=timezone.localtime(timezone.now()).date())
        past_reservations.delete()

        # Возвращаем актуальный queryset
        return Reservation.objects.all()

    @swagger_auto_schema(operation_summary="Get list of reservations")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Create a new reservation")
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
