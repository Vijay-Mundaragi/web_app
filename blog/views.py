from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
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
									 #  object in place of posts as this is default name 
	ordering = ['-date_posted'] 
	paginate_by = 5


class UserPostListView(ListView):
	model = Post
	template_name = 'blog/user_posts.html'
	context_object_name = 'posts'					
	paginate_by = 5

	#overriding the query set method to return only posts of particular user
	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('-date_posted')


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