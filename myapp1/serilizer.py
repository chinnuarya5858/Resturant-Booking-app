from rest_framework import serializers
from .models import Table1,Booking

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model=Table1
        fields='__all__'
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Booking
        fields='__all__'
        