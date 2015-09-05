from django.shortcuts import render

# Create your views here.

from nblog.models import Post,Category,Author
from django.shortcuts import render_to_response, get_object_or_404
from django.utils import timezone

def home(request):
  posts = Post.objects.filter(date__lte=timezone.now()).order_by('date')
  author= Author.objects.get()
  return render(request, 'blog/home.html', {'author': author, 'posts': posts})

def post(request):
  print "reuqest in post"
  print request.path[1::]
  post = Post.objects.get(url=request.path[1::])
  author= Author.objects.get()
  return render(request, 'blog/post.html', {'post': post, 'author': author})
