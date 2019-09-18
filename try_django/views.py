from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail

def home_page(request):
    my_title= "Home page"
    return render(request, "home_page.html", {"title": "Home"})

def about_page(request):
    return render(request, "about_page.html", {"title": "About"})
    
def contact_page(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        send_mail(
            'Contact',
            form.cleaned_data,
            'mace@example.com',
            ['mace@example.com'],
            fail_silently=False,
        )
        form = ContactForm()
    context = {
        "title": "Contact", 
        "form": form
    }
    return render(request, "form.html", context)
    
def links_page(request):
    return render(request, "links_page.html", {"title": "Links"})
