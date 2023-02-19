from rest_framework.serializers import ModelSerializer
from .models import Papeleta

class PapeleetaSerializer(ModelSerializer):
    class Meta:
        model = Papeleta
        fields = ['id', 'timestamp', 'comentarios']