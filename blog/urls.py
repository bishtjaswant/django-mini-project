from django.urls import  path
from  blog import views

urlpatterns = [
      
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("dashboard/", views.dashboard ,name="dashboard"),
    path("login/", views.loginuser, name="login"),
    path("logout/", views.logoutuser, name="logout"),
    path("create/", views.createaccount, name="create"),
]
