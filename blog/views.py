from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from blog.models import Post
from blog.forms import SignUpForm,LoginForm,PostForm

# Create your views here.
def home(request):
    posts = Post.objects.all()
    context = {}
    context['posts']=posts
    return render(request,'blog/home.html',context)



def about(request):
    return render(request,'blog/about.html')



def contact(request):
    return render(request,'blog/contact.html')



def dashboard(request):

    if  request.user.is_authenticated:    
        posts  = Post.objects.all()
        context={}
        context['posts']=posts
        return render(request,'blog/dashboard.html',context)
    else:
        messages.success(request,'your request denied due to unauthorize access.you need to login first access this page')
        return HttpResponseRedirect('/login/')




def addpost(request):
    if   request.user.is_authenticated:    

        if request.method=='GET':
            form= PostForm()
            context = {}
            context['form']=form
            return render(request,'blog/addpost.html',context)
        

        if request.method=='POST':
            form= PostForm(data=request.POST)
            if form.is_valid():
                title  = form.cleaned_data['title']
                description = form.cleaned_data['description']
                obj = Post(title=title,description=description)
                obj.save()
                messages.success(request,'Your post saved')
                return HttpResponseRedirect('/dashboard/')
            context = {}
            context['form']=form
            return render(request,'blog/addpost.html',context)
    else:
        messages.success(request,'you can not add post. you need to login first access this page')
        return HttpResponseRedirect('/login/')


def updatepost(request,post_id):
    if   request.user.is_authenticated: 
        if request.method=='GET':
            post = Post.objects.get(pk=post_id)
            form  = PostForm(instance=post)
            context = {}
            context['form'] = form
            context['data'] = post 
            return render(request,'blog/updatepost.html',context)
            
        
        if request.method=='POST':
            post = Post.objects.get(pk=post_id)
            form  = PostForm(request.POST,  instance=post)
            if form.is_valid():
                form.save()
                messages.success(request,'Your post updated')
                return HttpResponseRedirect('/dashboard/')
    else:
        messages.success(request,'you can not update someone\'s  post')
        return HttpResponseRedirect('/login/')
       
 

def deletepost(request,post_id):
    if   request.user.is_authenticated: 
        post= Post.objects.get(pk=post_id)

        if post.delete():
            messages.success(request,'your post has been removed')
            return HttpResponseRedirect('/dashboard/')
        else:
            messages.success(request,'something went wrong, try again')
            return HttpResponseRedirect('/dashboard/')
    else:
        messages.success(request,'you can not delete someone\'s  post')
        return HttpResponseRedirect('/login/')
       


def loginuser(request):
    if  not request.user.is_authenticated:    
        print(request.user)        
        form = LoginForm()
        if request.method=="POST":
            form = LoginForm(request,data=request.POST)
            if form.is_valid():
                un= form.cleaned_data.get('username')
                pwd = form.cleaned_data.get('password')
                user= authenticate(request,username=un,password=pwd)
                if user is not None:
                    login(request,user=user)
                    return HttpResponseRedirect('/dashboard/')
        context = {}
        context['form']=form
        return render(request,'blog/login.html',context)
    else:
        return  HttpResponseRedirect('/dashboard/')



def createaccount(request):
    form = SignUpForm()
    if request.method=='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'your account created. now you can login into your account')
            return HttpResponseRedirect('/login')
    context = {}
    context['form']=form
    return render(request,'blog/signup.html',context)




def logoutuser(request):
    logout(request)
    messages.success(request,'you are  loggedout now  succesfully')
    return HttpResponseRedirect('/login/')

