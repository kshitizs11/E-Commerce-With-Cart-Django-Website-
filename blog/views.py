from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogpost
# Create your views here.
def index (request):
    myposts = Blogpost.objects.all()
    return render(request, 'blog/index.html')
# by using id we arereceiving id from our url individually
#we are gathering post corresponding to that id
def blogpost(request,id):
    post = Blogpost.objects.filter(post_id=id)[0]
    #now we are sending our post to our template
    return render(request, 'blog/blogpost.html',{'post',post})
    #now WE are sending this to our html and where we are reeving the data
#this is a way of recieving data from data from data base
