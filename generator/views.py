from rest_framework import viewsets
from pdf.utils.util import create_response
from .serializer import GeneratePdfSerializer

class GeneratePdfViewSet(viewsets.ViewSet):

    def create(self, request):
        validate = GeneratePdfSerializer(data=request.data)
        validate.is_valid(raise_exception=True)
        try:
            result = validate.generate_ticket()
            if result['success']:
                return create_response(True, 201, '', result['message'], 0)
            else:
                return create_response(False, 500, '', result['message'], 0)
        except Exception as err:
            return create_response(False, 500, {}, err, 0)
