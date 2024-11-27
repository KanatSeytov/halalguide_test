from rest_framework import serializers

from .models import PointOfInterest

def validate_latitude(value):
    if not -90 <= value <= 90:
        raise serializers.ValidationError("Latitude must be between -90 and 90.")
    return value

def validate_longitude(value):
    if not -180 <= value <= 180:
        raise serializers.ValidationError("Longitude must be between -180 and 180.")
    return value


class PointOfInterestSerializer(serializers.ModelSerializer):

    latitude = serializers.FloatField(validators=[validate_latitude])
    longitude = serializers.FloatField(validators=[validate_longitude])

    class Meta:
        model = PointOfInterest
        fields = '__all__'
