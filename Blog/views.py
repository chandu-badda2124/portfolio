from django.shortcuts import render,redirect
from django.core.paginator import Paginator

# Create your views here.
from .models import BlogPost,Project,ContactMessage
from .forms import ContactForm


def home(request):
    posts = BlogPost.objects.all().order_by('-date_posted')
    projects = Project.objects.all()
    return render(request, 'home.html', {'posts': posts,'projects': projects,})

def blog(request):
    posts_list = BlogPost.objects.all().order_by('-date_posted')
    paginator = Paginator(posts_list, 5)  # Show 5 posts per page
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    return render(request, 'blog.html', {'posts': posts})

def blog_detail(request, pk):
    post = BlogPost.objects.get(id=pk)
    return render(request, 'blog_detail.html', {'post': post})

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})

def deleteBlog(request,pk):
    blog=BlogPost.objects.get(id=pk)
    blog.delete()
    return render(request, 'blog_detail.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            ContactMessage.objects.create(name=name, email=email, message=message)
            return redirect('contact_success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def contact_success(request):
    return render(request, 'contact_success.html')