from django.contrib.auth import get_user_model

from rest_framework.serializers import ModelSerializer

User = get_user_model()


class RasterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["raster"]

    def save(self, *args, **kwargs):
        # if self.instance.raster:
        #     self.instance.raster.delete()
        return super().save(*args, **kwargs)