from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import time


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Menu(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Menu"


class Reservation(models.Model):
    guests = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    date = models.DateField()
    time = models.TimeField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    special_request = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def clean(self):
        if Reservation.objects.filter(date=self.date).count() >= 50:
            raise ValidationError("No available tables for this date. The nearest available date is tomorrow.")

        if not (time(9, 0) <= self.time <= time(21, 0)):
            raise ValidationError("Booking available only between 9:00 and 21:00.")

        if self.date < timezone.now().date():
            raise ValidationError("Cannot book for past dates.")

        if self.date == timezone.now().date() and self.time < timezone.localtime(timezone.now()).time():
            raise ValidationError("Cannot book for past times.")

        if Reservation.objects.filter(date=self.date, phone_number=self.phone_number).exists():
            raise ValidationError("A reservation with this phone number already exists for this date.")
