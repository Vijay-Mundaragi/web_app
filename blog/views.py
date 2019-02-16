from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
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


class PostCreateView(LoginRequiredMixin, CreateView):	#view with a form where we create a new post
	model = Post
	fields = ['title', 'content']

	#overriding from_valid method else we get not_null constraint failed error (NOT NULL constraint failed)
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):	#view with a form where we create a new post
	model = Post
	fields = ['title', 'content']

	#overriding from_valid method else we get not_null constraint failed error (NOT NULL constraint failed)
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		#to restrict update post only to author of particular post
		#get the exact post we are currently updating
		post = self.get_object() #get_oject is method of UpdateView
		if self.request.user == post.author:
			return True
		return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = '/'

	def test_func(self):
		#to restrict update post only to author of particular post
		#get the exact post we are currently updating
		post = self.get_object() #get_oject is method of UpdateView
		if self.request.user == post.author:
			return True
		return False





def about(request):
	return render(request, "blog/about.html")





'''
for function based views we can use @login_required decorator
@login_required decorator cant be used for class based decorator
inherit LoginRequiredMixin for class based views for only logged in users to access the route

'''