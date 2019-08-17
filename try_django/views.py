from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    my_title= "Home page"
    return render(request, "home_page.html", {"title": my_title})

def about_page(request):
    return render(request, "about_page.html", {"title": "About"})
    
def contact_page(request):
    return render(request, "form.html", {"title": "Contact"})
    
def links_page(request):
    return render(request, "links_page.html", {"title": "Links"})
