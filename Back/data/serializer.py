from rest_framework import serializers
from data.models import Data
from trasation.serializer import TransationSerializer
from trasation.models import Trasation
import ipdb
class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ["id","store_owner","store_name", "recipient_cpf", "card", "value", "date", "hour", "type"]
        read_only_fields = ["id"]