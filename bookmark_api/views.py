from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from  django.http import HttpResponse,JsonResponse
from  rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from  rest_framework.views import APIView
from  rest_framework import filters,viewsets
from rest_framework.response import Response
from django.db.models import Model
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from   .models import Bookmarks,tags
from .serializers import bookmarksapi,tagapi

# Create your views here.
class Create_bookmark(APIView):
    def get_object(self):
        try:
            return Bookmarks.objects.all()
        except Bookmarks.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    def get(self,request):
        q = self.get_object()
        print(100)
        print(q)
        p = bookmarksapi(q)
        return Response(p.data)
    def put(self,request):
        w = Bookmarks.objects.all()
        a = bookmarksapi(w,data=request.data)
        if a.is_valid():
            a.save()
            return Response(a.data)
        return Response(a.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request):
        q = self.get_object()
        q.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Create_and_delete_bookmarks(APIView):
    def get_object(self):
        try:
            return Bookmarks.objects.all()
        except Bookmarks.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    def get(self, request):
        q = self.get_object()
        print(100)
        print(q)
        p = bookmarksapi(q,many=True)
        return Response(p.data)
    def post(self, request):
        s = bookmarksapi(data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data, status=status.HTTP_201_CREATED)
        return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request):
        q = self.get_object()
        q.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    def put(self,request):
        w = Bookmarks.objects.all()
        a = bookmarksapi(w,data=request.data)
        if a.is_valid():
            a.save()
            return Response(a.data)
        return Response(a.errors, status=status.HTTP_400_BAD_REQUEST)
class Create_tags(APIView):
    def get_object(self,tag_id):
        try:
            return tags.objects.filter(tag_id=tag_id)
        except tags.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    def get(self,request,tag_id):
        q = self.get_object(tag_id)
        print(100)
        p = tagapi(q,many=True)
        print(p)
        return Response(p.data)

    def post(self, request,tag_id):
        s = tagapi(data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data, status=status.HTTP_201_CREATED)
        return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request):
        q = self.get_object()
        q.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)