from django.shortcuts import render
from .models import studentDetails
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import studentSerializers
# Create your views here.

def home(request):
    return render(request,'pj.html')

def registrationPage(request):
    return render(request,'reges.html')
def coursespage(request):
    return render(request,'courses.html')
def aboutus(request):
    return render(request,'text.html')
def contactus(request):
    return render(request,'contact.html')
class studentInfo(APIView):
    
    def get(self,request):
            students = studentDetails.objects.all()
            serializer = studentSerializers(students,many = True)
            return Response({"studentlist":serializer.data})
    def post(self,request):
            student = request.data.get('studentDetails')
            Serializers = studentSerializers(data=student)
            if Serializers.is_valid(raise_exception=True):
                student_obj=Serializers.save()
            return Response({"studentDetails":Serializers.data})