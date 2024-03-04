from django.utils import timezone
from django.http import JsonResponse
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Menu, Category, Reservation
from .serializers import MenuSerializer, CategorySerializer, ReservationSerializer


class MenuListView(generics.ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class DishDetailView(generics.RetrieveAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    lookup_field = 'id'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryMenuListView(generics.ListAPIView):
    serializer_class = MenuSerializer

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return Menu.objects.filter(categories__id=category_id)


class ReservationListView(generics.ListCreateAPIView):
    serializer_class = ReservationSerializer

    def get_queryset(self):
        # Удаляем прошлые бронирования перед выполнением запроса
        past_reservations = Reservation.objects.filter(date__lt=timezone.localtime(timezone.now()).date())
        past_reservations.delete()

        # Возвращаем актуальный queryset
        return Reservation.objects.all()
