from django.contrib import admin
from .models import Blog, Comment #덧글기능 추가


admin.site.register(Blog)
admin.site.register(Comment) #덧글기능 추가
