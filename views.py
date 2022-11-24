from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context = {
        "title":"Trigger python logic"
        }
    return render(request, "home/home.html", context)

def simple_function(request):
    print("\nThis is a simple function\n")
    return HttpResponse("""<html><script>window.location.replace('/');</script></html>""")

