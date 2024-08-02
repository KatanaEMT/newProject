from django.shortcuts import render
from rest_framework.views import APIView
from .models import Publication
from posts.serializers import PublicationSerializer
from rest_framework.response import Response


class List(APIView):
    def get(self, request, *args, **kwargs):
        publication_list = Publication.objects.all()
        serializer = PublicationSerializer(instance=publication_list, many=True)
        return Response(data=serializer.data)


class Detail(APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs["pk"]
        publication_object = Publication.objects.get(pk=pk)
        serializer = PublicationSerializer(publication_object)
        return Response(serializer.data)

