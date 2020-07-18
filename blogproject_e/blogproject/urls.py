from django.contrib import admin
from django.urls import path
import blogapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogapp.views.home, name="home"),
    path('<int:blog_id>', blogapp.views.detail, name="detail"),
    path('new/', blogapp.views.new, name="new"),
    path('blogapp/create/', blogapp.views.create, name="create"),
    path('blogapp/Comment/(?P<blog_id>[0-9]+)$', blogapp.views.comment, name="comment"),    
]
