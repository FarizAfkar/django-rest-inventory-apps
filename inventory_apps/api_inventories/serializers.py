from rest_framework import serializers
from django.conf import settings
from .models import Inventory

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)

class TokenRefreshSerializer(serializers.Serializer):
    refresh = serializers.CharField(required=True, write_only=True)


class InventoryCreate(serializers.ModelSerializer):
    image = serializers.ImageField()
    class Meta:
        model = Inventory
        fields = [
            'name', 'quantity', 'serial_number', 'additional_info',
            'image', 'created_by', 'updated_by'
        ]

    def validate_image(self, image):
        if image:
            if image.content_type not in settings.ALLOWED_IMAGE_TYPES :
                raise serializers.ValidationError("Only JPG and PNG formats are allowed.")
        return image

class InventoryDetail(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = '__all__'

class InventoryUpdate(serializers.ModelSerializer):
    image = serializers.ImageField()
    class Meta:
        model = Inventory
        fields = [
            'name', 'quantity', 'serial_number', 'additional_info',
            'image', 'updated_by'
        ]

    def validate_image(self, image):
        if image:
            if image.content_type not in settings.ALLOWED_IMAGE_TYPES :
                raise serializers.ValidationError("Only JPG and PNG formats are allowed.")
        return image
