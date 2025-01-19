from django.shortcuts import render
from rest_framework.views import APIView,Response
from .models import Category
from django.core.serializers import serialize
import json
# Create your views here.
class AllCategories(APIView):
    def get(self,request):
        categories = Category.objects.order_by("name")
        serialized = serialize('json', categories)
        category_json = json.loads(serialized)
        return Response(category_json)
    def post(self,request):
        new_category = Category.objects.create(**request.data)
        serialized = serialize('json', [new_category])
        return Response(json.loads(serialized))

class CategoryById(APIView):
    def get():
        pass
    def put():
        pass
    def delete():
        pass

class AllPostsInCategory(APIView):
    def get():
        pass
    def post():
        pass

class PostById(APIView):
    def get():
        pass
    def put():
        pass
    def delete():
        pass