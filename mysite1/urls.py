"""mysite1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from register import views
from django.conf.urls import url

app_name='register'
urlpatterns = [
   # path('admin/', admin.site.urls),
    #path('',views.home),
    path('',include('register.urls')),
    url(r'courses.html$',views.coursespage),
    #path('courses.html/reges.html',views.registrationPage),
    url(r'reges.html$',views.registrationPage),
    url(r'registerpageAction$',views.studentInfo.as_view()),
    url(r'academics.html$',views.coursespage),
    url(r'pj.html$',views.home),
   # url(r'text.html$',views.aboutus),
    url(r'contact.html$',views.contactus),
  #  path('academics.html',views.coursespage),
    url(r'text.html$',views.aboutus),
]
