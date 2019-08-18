from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm

def home_page(request):
    my_title= "Home page"
    return render(request, "home_page.html", {"title": my_title})

def about_page(request):
    return render(request, "about_page.html", {"title": "About"})
    
def contact_page(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm()
    context = {
        "title": "Contact", 
        "form": form
    }
    return render(request, "form.html", context)
    
def links_page(request):
    return render(request, "links_page.html", {"title": "Links"})
