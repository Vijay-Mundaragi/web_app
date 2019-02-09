from django.shortcuts import render
# Create your views here.

posts = [
	{
		"author": "Author 1",
		"title": "Post 1",
		"content": " The only time success comes before work is in the dictionary....",
		"date_posted": "February 9, 2019"
	},
	{
		"author": "Author 2",
		"title": "Post 2",
		"content": " I know people usually better than they know themselves",
		"date_posted": "February 8, 2019"
	}
]



def home(request):
	context = {
		"posts": posts
	}
	return render(request, "blog/home.html", context)


def about(request):
	return render(request, "blog/about.html")