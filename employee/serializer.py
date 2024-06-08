from rest_framework import serializers

class EmpSerializer(serializers.ModelSerializer):
    class Meta :
        model = Employee
        fields = _all_