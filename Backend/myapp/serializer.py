from rest_framework import serializers

from .models import Property, Image, Address, User


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['imageData', 'filename']


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['country', 'city', 'postcode', 'floor']


class PropertySerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    images = serializers.SerializerMethodField()

    class Meta:
        model = Property
        fields = '__all__'

    def get_images(self, obj):
        image_ids = obj.images

        images = Image.objects.filter(_id__in=image_ids)

        return ImageSerializer(images, many=True).data


class UserSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = '__all__'

    def get_images(self, obj):
        image_ids = obj.images

        images = Image.objects.filter(_id__in=image_ids)

        return ImageSerializer(images, many=True).data
