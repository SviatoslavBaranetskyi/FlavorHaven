from rest_framework import serializers
from .models import Menu, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class MenuSerializer(serializers.ModelSerializer):
    categories = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='name',
        many=True
    )

    class Meta:
        model = Menu
        fields = '__all__'
