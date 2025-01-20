from django.shortcuts import render
from rest_framework.views import APIView,Response
from .models import Category, Post
from django.core.serializers import serialize
from .serializer import PostSerializer
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
    def get(self, request, category_id):
        category = Category.objects.get(id=category_id)
        serialized= serialize('json', [category])
        json_cat= json.loads(serialized)
        return Response(json_cat)
    
    def put(self, request, category_id):
        category = Category.objects.get(id=category_id)
        category.name = request.data['name']
        serialized = serialize('json',[category])
        json_category = json.loads(serialized)
        return Response(json_category)
        

    def delete(self, request,category_id):
        category = Category.objects.get(id=category_id)
        category.delete()
        return Response(f"The {category.name} category, has been deleted")
    
        

class AllPostsInCategory(APIView):
    def get(self, request, category_id):
        category = Category.objects.get(id=category_id)
        posts = category.get_posts()
        serializer =PostSerializer(posts, many=True)
    
        return Response(serializer.data)


    
    def post(self, request, category_id):
        category = Category.objects.get(id=category_id)
        post_data = request.data.copy()
        post_data["category"] = category.id
        serializer = PostSerializer(data=post_data)
        if serializer.is_valid():
            new_post = serializer.save()
            
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class PostById(APIView):
    def get(self, request, category_id, post_id):
        category = Category.objects.get(id=category_id)
        post = Post.objects.get(id=post_id)
        if post in category.get_posts():
            serialized=serialize("json", [post])
            json_post = json.loads(serialized)
            return Response(json_post)
        return Response(f"post not in this category")
        
    def put(self, request, post_id):
        post = Post.objects.get(id=post_id)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
    def delete(self, request,category_id, post_id):
        post = Post.objects.get(id=post_id)
        post.delete()
        return Response(f"The post titled '{post.title}' has been deleted")
        