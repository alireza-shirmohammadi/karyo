
from django.urls import path
from .views import home, about, contact, blog, detailBlog, category,contact_form

urlpatterns = [
    path('', home,name='home'),
    path('about', about),
    path('contact', contact),
    path('blog', blog, name='blog'),
    path('<slug:slug>',detailBlog, name="detailBlog"),
    path('<slug:slug>', category, name="category"),
    path('contact/submit',contact_form,name='contact_form'),

]
