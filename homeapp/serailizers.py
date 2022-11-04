from rest_framework import serializers
from .models import Obj

class PersonSerailizers(serializers.ModelSerializer):
    class Meta:
        model=Obj
        fields = '__all__'
        
