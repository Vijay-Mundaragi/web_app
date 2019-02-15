from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.

def home(request):
	context = {
		"posts": Post.objects.all()
	}
	return render(request, "blog/home.html", context)


class PostListView(ListView):
	model = Post 	# what model to query inorder to create the list
	template_name = 'blog/home.html' # returns looks for <app>/<model>_<view_type>.html by default
	context_object_name = 'posts'	 #  in our template we are iterating over variable posts. if we omit this, we need to include 
									 #  object_list in place of posts as this is default name 
	ordering = ['-date_posted'] 


class PostDetailView(DetailView):
	model = Post


def about(request):
	return render(request, "blog/about.html")