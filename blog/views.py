from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(reuest):
	return HttpResponse("<h1> Blog Home </h1>")


def about(reuest):
	return HttpResponse("<h1> Blog About </h1>")