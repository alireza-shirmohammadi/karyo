import json

from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect

from Karyo import settings
from .models import Article, Category


# Create your views here.


def home(request):
    return render(request, "blog/index.html")



def about(request):
    return render(request, "blog/about.html")



def contact(request):
    return render(request, "blog/contact.html")



def blog(request):
    context = {
        'articles': Article.objects.published(),
    }
    return render(request, 'blog/blog.html', context)



def detailBlog(request,slug):
    context = {
        'article': get_object_or_404(Article.objects.published(), slug=slug)
    }
    return render(request, 'blog/single.html', context)


def category(request,slug):
    context = {
        'category': get_object_or_404(Category, slug=slug, status="True")
    }
    return render(request, 'blog/category.html', context)



def contact_form(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        website=request.POST.get('website')
        message=request.POST.get('message')
        print(request.POST)

        admins_email = [user.email for user in User.objects.filter(is_superuser=True)]
        message = {'name':name,'email':email,"phone":phone,"website":website,"message":message}


        subject='سفارش طراحی سایت'
        message= json.dumps(message,ensure_ascii=False)
        print(message)
        print(type(message))
        email_from=settings.EMAIL_HOST_USER
        emails=admins_email
        send_mail(subject,message,email_from,emails)
        print('done')
        return redirect('home')