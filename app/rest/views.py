from django.shortcuts import render
from rdb.models import DuplexFrequencyPair,Repeater
from rest.serializers import DFPSerializer,RepeaterSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
# Create your views here.



class DFPView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
   
    def get(self, request):
        data={
            'response':'no get view available for now',
        }
       
        return Response(data)

    def post(self, request):
        serializer = DFPSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RepeaterView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
   
    def get(self, request):
        data={
            'response':'no get view available for now',
        }
       
        return Response(data)

    def post(self, request):
        serializer = RepeaterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)