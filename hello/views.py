
from .models import BlogPost
from django.http import HttpResponse
from django.shortcuts import render
import re
from datetime import datetime

def home(request):
    return render(request, 'hello/home.html')
def hello(request):
    return HttpResponse("Hello, Django!")
def about(request):
    # Ihre Logik hier, zum Beispiel:
    return render(request, 'hello/about.html')
def contact(request):
    # Ihre Logik hier, zum Beispiel:
    return render(request, 'hello/contact.html')
def it_is_me(request):
    return HttpResponse("Hello, it's me, hi I'm the HttpResponse!")

def hello_there(request, name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "! It's " + formatted_now
    return HttpResponse(content)
import logging

# Erstellen Sie eine Instanz des Loggers mit dem Namen Ihrer App oder eines anderen sinnvollen Namens.
logger = logging.getLogger(__name__)

def some_view(request):
    # Hier kommt die Logik Ihrer View.
    
    # Eine Info-Log-Nachricht erstellen.
    # Dies ist hilfreich, um den Durchlauf durch den Code zu verfolgen oder wichtige Ereignisse zu protokollieren.
    logger.info('Information message')
    
    # Rendern Sie Ihr Template und geben Sie es als HttpResponse zurück.
    return render(request, 'template_name.html')

def blog_posts(request):
    posts = BlogPost.objects.all()
    return render(request, 'hello/blog_posts.html', {'posts': posts})