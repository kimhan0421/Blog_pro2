from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog, Comment 
from django.urls import reverse


def home(request):
    blogs = Blog.objects
    return render(request,'home.html', {'blogs': blogs})

def detail(request, blog_id):
    detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blogapp': detail})

def new(request): #new.html을 띄워줌
    return render(request, 'new.html')

def create(request): #입력받은 내용을 디비에 넣어주는 함수
    blog=Blog()
    blog.title=request.GET['title']
    blog.body=request.GET['body']
    blog.pub_date=timezone.datetime.now()# import timezone
    blog.save()#디비에 저장해라
    return redirect('/blog/'+str(blog.id))    

    
def comment(request, blog_id):
    if request.method == 'POST':
        if request.user.is_authenticated:
            comment = Comment()
            comment.comment = request.POST['inputComment']
            comment.pup_date = timezone.datetime.now()
            comment.author = request.user
            comment.blog = Blog.objects.get(id=blog_id)
            comment.save()
            return redirect('/blog/'+str(blog_id))
        else:
            return redirect('login')
    else:
        return HttpResponseNotFound("없는 페이지 입니다.")
        
