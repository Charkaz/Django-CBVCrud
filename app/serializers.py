from rest_framework import serializers
from .models import Kitab

class KitabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kitab
        fields = ['kitab_ad','kitab_onsoz','kitab_janr','kitab_seh','kitab_yazar','stokda','sekil'] 
