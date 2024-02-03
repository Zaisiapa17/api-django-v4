from rest_framework import serializers

from . import test_img_model

class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = test_img_model.Picture
        fields = ('img_name')