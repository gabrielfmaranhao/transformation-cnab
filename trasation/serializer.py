from rest_framework import serializers
from data.models import Data
from .models import Trasation
import ipdb

class TransationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trasation
        fields = ["id","type","description", "nature", "signal"]
        read_only_fields = ["id"]
    