from rest_framework import serializers
from .models import Hit

class HitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hit
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at', 'title_url')