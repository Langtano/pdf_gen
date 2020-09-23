from rest_framework import serializers
from .dao_generator import GeneratePdfDao

class GeneratePdfSerializer(serializers.Serializer):
    report = serializers.CharField()
    name = serializers.CharField(required=True)
    rfc = serializers.CharField()
    address = serializers.CharField()
    user = serializers.CharField()
    currency = serializers.CharField()
    plan = serializers.CharField()
    period = serializers.CharField()
    goal = serializers.CharField()
    data = serializers.ListField()
    total = serializers.CharField()

    def generate_ticket(self):
        result = GeneratePdfDao.generate_pdf(self, ticket=self.data)
        return result