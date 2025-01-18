from categories_app.models import Category, Post

category1 = Category.objects.create(name='pets')

post1 = Post.objects.create(category=category1, content="This is the cutest chinchilla you'll ever see!")
