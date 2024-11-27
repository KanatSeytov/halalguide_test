from django.db import models

# Create your models here.
class PointOfInterest(models.Model):
    name = models.CharField(max_length=60) #(String, название точки интереса).
    description = models.TextField() #(Text, описание).
    latitude = models.FloatField()
    longitude = models.FloatField() #(Float, географические координаты).
    category = models.CharField(max_length=155) #(String, категория точки, например, "ресторан", "мечеть").
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) #(DateTime, автоматически задаются).
