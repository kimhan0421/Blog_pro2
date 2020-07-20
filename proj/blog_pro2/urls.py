from django.contrib import admin
from django.urls import path
import blog.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home, name="home"),
    path('/likelion', blog.views.likelion, name="likelion"),
    path('blog/<int:blog_id>/', blog.views.detail, name="detail"),
    path('/like2019', blog.views.like2019, name="like2019"),
    path('/like2020', blog.views.like2019, name="like2020"),
]
