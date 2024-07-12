from job.models import Job, Portal
from rest_framework import serializers

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ["id", "titulo", "descricao", "modelo_contratacao", "senioridade", "site_busca"]


class PortalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portal
        fields = ["id", "nome", "url"]