from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Posts

def home(request):
    return render(request, 'home.html')

@login_required
def mypage(request):
    myposts = Posts.objects.filter(user = request.user.username)
    data = {"posts":myposts}
    return render(request, 'mypage.html', data)

@login_required
def newtxt(request):
    return render(request, 'newtxt.html', {})

def posts(request):
    allposts = Posts.objects.filter(read = True)
    data = {"posts":allposts}
    return render(request, 'posts.html', data)

def regist(request):
    if request.method == 'POST':
        post = Posts.objects.create(user = request.user.username)
        txt = request.POST['txt']
        if txt == '':   #もし、テキストエリアに何も書かれていなかったらリロード
            return render(request, 'newtxt.html', {})
        post.note = txt
        if request.POST.get('pub') :
            post.read = True
        
        post.save()
    return render(request,'home.html', {})