from django.shortcuts import Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import BlogPost



def blog_post_detail_page(request, slug):
    queryset = BlogPost.objects.filter(slug=slug)
    if queryset.count() == 0:
        raise Http404
    obj = queryset.first()
    # obj = get_object_or_404(BlogPost, slug=slug)   
    template_name = 'blog_post_detail.html'
    context = {'object':obj}
    return render(request, template_name, context) 
    
    
def blog_post_list_view(request):
    #list objects
    template_name = 'blog_post_list.html'
    context = {'object_list':[]}
    return render(request, template_name, context) 

def blog_post_create_view(request):
    #create objects
    template_name = 'blog_post_create.html'
    context = {'form':None}
    return render(request, template_name, context) 
   

def blog_post_detail_view(request, slug):
    # one object also known as details view 
    obj = get_object_or_404(BlogPost, slug=slug) 
    template_name = 'blog_post_detail.html'
    context = {'object':obj}
    return render(request, template_name, context) 
    

def blog_post_uodate_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug) 
    template_name = 'blog_post_update.html'
    context = {'object':obj, 'form':None}
    return render(request, template_name, context) 
    

def blog_post_delete_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug) 
    template_name = 'blog_post_delete.html'
    context = {'object':obj}
    return render(request, template_name, context) 