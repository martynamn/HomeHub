from rest_framework import serializers

from .models import Property, Image, Address


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['imageData', 'filename']


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['country', 'city', 'postcode', 'floor']


class PropertySerializer(serializers.ModelSerializer):
    image = ImageSerializer(allow_null=True)
    address = AddressSerializer()

    class Meta:
        model = Property
        fields = '__all__'
