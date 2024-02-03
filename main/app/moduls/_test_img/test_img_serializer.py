from rest_framework import serializers

from . import test_img_model

class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = test_img_model.Picture
        fields = '__all__'
    def get_img_name(self, obj):
        return str(obj.img_name)