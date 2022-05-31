from django.contrib import messages
from django.http import Http404
from django.shortcuts import redirect, render
from django.db.models import Q
from article.models import Article
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.core.paginator import Paginator
# Create your views here.


def index(request):
    
    article_list = Article.objects.all().order_by('-id')
    paginator = Paginator(article_list,4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request,'list.html',{'page_obj':page_obj})

def detail(request,article_id):
    article = Article.objects.get(id=article_id)
    return render(request,'detail.html',{'article':article})

def search(request):
    if request.method=='POST':
        title = request.POST['title']
        articles = Article.objects.filter(title__icontains=title)
        page_obj = articles 
    
    return render(request,'list.html',{'page_obj':page_obj})
@login_required(login_url='signin')
def upload(request):
    if request.method=='POST':
        author = request.user
        title = request.POST['title']
        content = request.POST['content']
        image = request.FILES.get('image_upload')

        new_article = Article.objects.create(author=author,title=title,content=content,image=image)
        new_article.save()
        return redirect('/')
    return render(request,'upload.html')
@login_required(login_url='signin')
def deletepost(request,article_id):
    if article_id is not None:
        article = Article.objects.filter(id=article_id)
        article.delete()
        return redirect('/my_articles')
    else:
        return redirect('/')
@login_required(login_url='signin')
def editpost(request,article_id):
    article = Article.objects.filter(id=article_id)
    return render(request,'edit.html',{'article':article})

def signup(request):
    if request.method=='POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email Already Exists')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username Already Exists')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                user_login = auth.authenticate(username=username,password=password)
                auth.login(request,user_login)
                return redirect('index')
        else:
            messages.info(request,'Passwords Are Not Matching')
            return redirect('signup')
    return render(request,'signup.html')

def signin(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Username or Password')
            return redirect('signin')
    else:
        return render(request,'signin.html')

@login_required(login_url='signin')
def logout(request):
    auth.logout(request)
    return redirect('signin')

@login_required(login_url='signin')
def my_page(request):
    author = request.user
    articles = Article.objects.filter(author=author)
    return render(request,'list.html',{'page_obj':articles})