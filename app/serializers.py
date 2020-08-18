from rest_framework import serializers
from.models  import Course,Subject,Teacher,Batch,Student

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Subject
        fields="__all__"     
        
class CourseSerializer(serializers.ModelSerializer):
        class Meta:
            model=Course
            fields=('id','name','duration','fees','subjects')

class BatchSerializer(serializers.ModelSerializer):
        class Meta:
            model=Batch
            fields="__all__"         

class TeacherSerializer(serializers.ModelSerializer):
        class Meta:
            model=Teacher
            fields="__all__"         

class StudentSerializer(serializers.ModelSerializer):
        class Meta:
            model=Student
            fields="__all__"         
