from client.models import Client
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta :
        model = Client
        fields = ['id','client_name','client_phone']