from rest_framework import serializers
from zztemp_codinghw2.models import zztemp_codinghw2


class zztemp_codinghw2_serializer(serializers.ModelSerializer):
    class Meta:
        model = zztemp_codinghw2
        fields = ('id',
                  'text1',
                  'text2')
