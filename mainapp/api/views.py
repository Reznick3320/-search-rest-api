from rest_framework import generics
from mainapp.models import Restapi
from .serializers import RestapiSerializer
# from rest_framework.views import APIView
# from rest_framework.response import Response

class TestApiView(generics.ListAPIView):
    queryset = Restapi.objects.all()
    serializer_class = RestapiSerializer





# class TestApiView(APIView):

#     def get(self, request, *args, **kwargs):
#         data = [
#             {'id': 1, 'kod': 'aaattgg'}, 
#             {'id': 2, 'kod': 'ccaaffftttggtttgggccttcc'}, 
#             {'id': 3, 'kod': 'gggtttggtttgttt'},
#             {'id': 4, 'kod': 'attcccaa'}, 
#             {'id': 5, 'kod': 'taaggttggtttggttccc'}, 
#             {'id': 6, 'kod': 'gtttcacttgatcgg'},
#             {'id': 7, 'kod': 'atcgattggccaaaa'}, 
#             {'id': 8, 'kod': 'ggtttaacccttttaaaaccc'}, 
#             {'id': 9, 'kod': 'tttccccggggaaagg'}
#         ]
#         return Response(data)