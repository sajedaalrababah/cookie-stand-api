from rest_framework import serializers
from .models import cookie_stand


class cookie_standSerializer(serializers.ModelSerializer):
    class Meta:
        model = cookie_stand
        fields = "__all__"
