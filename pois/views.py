from rest_framework import viewsets, generics
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import PointOfInterestSerializer
from .models import PointOfInterest


class PointOfInterestViewSet(viewsets.ModelViewSet):

    queryset = PointOfInterest.objects.all()
    serializer_class = PointOfInterestSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']
