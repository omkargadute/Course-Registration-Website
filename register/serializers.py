from rest_framework import serializers
from .models import studentDetails
class studentSerializers(serializers.Serializer):
    stud_fname = serializers.CharField(max_length=100)
    stud_sname = serializers.CharField(max_length=100)
    stud_gender = serializers.CharField(max_length=10)
    stud_email = serializers.CharField(max_length=100)
    stud_course = serializers.CharField(max_length=100)

    def create(self,data):
        return studentDetails.objects.create(**data)
       