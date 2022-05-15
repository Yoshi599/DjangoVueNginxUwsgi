from django.shortcuts import render

# Create your views here.
# Yoshi

from rest_framework import status, viewsets, filters
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView        #Yoshi

class GetTestAPI(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        return Response(data={'status': 'Hello World!'}, status=status.HTTP_200_OK)