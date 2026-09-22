

from rest_framework import serializers
from api.models import User,Profile,Address

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["id","username","password","email","phone"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["id","username","password","email","phone"]

    def create(self, validated_data):
        return User.objects.create_superuser(**validated_data)


class UserProfileserializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField(read_only=True)
    class Meta:
        model=Profile
        fields="__all__"
        read_only_fields=["id","created_at","updated_at","user"]

class AddressSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField(read_only=True)
    class Meta:
        model=Address
        fields="__all__"
        read_only_fields=["id","created_at","updated_at","user"]
