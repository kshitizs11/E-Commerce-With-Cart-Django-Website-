from django.contrib import admin
from django.urls import path
from .import views
#by using <int:id> we can grab post individually
urlpatterns = [
    path("",views.index,name="blogHome"),
    path("blogpost/<int:id>",views.blogpost,name="blogPost")
]



#views ----> urls
#admin me register ------> models