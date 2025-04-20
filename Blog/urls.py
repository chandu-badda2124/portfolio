from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('Projects/', views.projects, name='projects'),
    path('Contact/', views.contact, name='contact'),
    path('success/', views.contact_success, name='contact_success'),
    path('deleteBlog/<int:pk>/', views.deleteBlog, name='delete_blog'),
]