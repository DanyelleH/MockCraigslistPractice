from django.shortcuts import render
from rest_framework.views import APIView,Response
from .models import Category
from django.core.serializers import serialize
import json
# Create your views here.
class AllCategories(APIView):
    def get(self,request):
        categories = Category.objects.all()
        serialized = serialize('json', categories)
        category_json = json.loads(serialized)

        return Response(category_json)