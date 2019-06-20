from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import time
from .models import Comment
 
# Create your views here.
def landing_page(request):
    return HttpResponse("success")

def today(request):
    html = "today.html"
    response = {
        "today" : time.ctime()
    }
    return render(request, html, response)

def comments(request):
    html = "comment.html"
    response = {
        "comments" : Comment.objects.all()
    }
    return render(request, html, response)

def add_comment(request):
    if request.method == "POST":
        name = request.POST["name"]
        comment = request.POST["comment"]
        Comment.objects.create(
            name=name,
            comment=comment
        )
    return HttpResponseRedirect("/landing-page/comments")
