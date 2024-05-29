from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta :
        model = Client
        fields = _all_