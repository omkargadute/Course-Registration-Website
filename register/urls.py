from register import views
from django.urls import path,include

urlpatterns = [
    path('',views.home),
    path('reges.html/',views.registrationPage),
    path('courses.html',views.coursespage),
    path('courses.html/reges.html',views.registrationPage),
    path('reges.html/registerpageAction',views.studentInfo.as_view()),

]