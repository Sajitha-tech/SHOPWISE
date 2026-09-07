

from rest_framework import serializers
from api.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["id","username","password","email","phone"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)