from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    return render(request,'blog/home.html')



def about(request):
    return render(request,'blog/about.html')



def contact(request):
    return render(request,'blog/contact.html')



def dashboard(request):
    pass



def loginuser(request):
    pass



def logoutuser(request):
    return HttpResponseRedirect('/')


def createaccount(request):
    pass

