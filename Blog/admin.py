from django.contrib import admin

# Register your models here.
from .models import BlogPost, Project, ContactMessage

admin.site.register(BlogPost)
admin.site.register(Project)
admin.site.register(ContactMessage)