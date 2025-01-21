from django.shortcuts import render
from rest_framework.views import APIView,Response
from .models import Category, Post
from django.core.serializers import serialize
from .serializer import PostSerializer, CategorySerializer
import json
# Create your views here.
class AllCategories(APIView):
    def get(self,request):
        categories = Category.objects.order_by("name")
        serialized = serialize('json', categories)
        category_json = json.loads(serialized)
        return Response(category_json)
    def post(self,request):
        name = request.data.get('name', None)
        if not name:
            return Response({"error": "name field is required"}, status=400)
        
        if Category.objects.filter(name=name):
            return Response({"error": "Category already exists"}, status=400)
        new_category = Category.objects.create(name=name)
        serializer = CategorySerializer(new_category) 
        return Response(serializer.data, status=201)


class CategoryById(APIView):
    def get(self, request, category_id):
        category = Category.objects.filter(id=category_id).first()
        if category:
            serializer = CategorySerializer(category)
            return Response(serializer.data, status=200)
        return Response({"error":"Category with that id does not exist"}, status=400)
    
    def put(self, request, category_id):
        category = Category.objects.filter(id=category_id).first()
        if category:
            if 'name' not in request.data:
                return Response({"error": "'name' field is required."}, status=400)
            category.name = request.data.get('name')
            category.save()
            serializer = CategorySerializer(category)
            return Response(serializer.data, status=200)
        return Response({"error":"Category does not exist."}, status=400)
        

    def delete(self, request,category_id):
        category = Category.objects.get(id=category_id)
        if category:
            category.delete()
            return Response(f"The {category.name} category, has been deleted", status=200)
        return Response("Category does not exist", status=400)
    


class AllPostsInCategory(APIView):
    def get(self, request, category_id):
        category = Category.objects.get(id=category_id)
        posts = category.get_posts()
        if posts:
            serializer =PostSerializer(posts, many=True)
            return Response(serializer.data, status=200)
        return Response("No posts in this category", status=400)

    
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
        category = Category.objects.filter(id=category_id).first()
        post = Post.objects.filter(id=post_id).first()
        if post in category.get_posts():
            serializer = PostSerializer(post)
            return Response(serializer.data, status= 200)
        return Response(f"Post with the id of {post_id} does not exist in this category", status=400)
        
    def put(self, request, category_id, post_id):
        post = Post.objects.filter(id=post_id).first()
        if post:
            serializer = PostSerializer(post, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=200)
        return Response({"error": "Post with id {post_id} does not exist"}, status=400)
       
        
    def delete(self, request,category_id, post_id):
        post = Post.objects.get(id=post_id)
        if post:
            post.delete()
            return Response(f"The post titled '{post.title}' with an id of {post_id} has been deleted", status=200)
        return Response("Post does not exist", status=400)
        