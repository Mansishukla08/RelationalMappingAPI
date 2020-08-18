from django.shortcuts import render
from rest_framework import viewsets
from .models import Course,Subject,Teacher,Student,Batch
from .serializers import CourseSerializer,SubjectSerializer,BatchSerializer,TeacherSerializer,StudentSerializer
# Create your views here.

class Courseinfo(viewsets.ModelViewSet):
    queryset =Course.objects.all()
    serializer_class=CourseSerializer
    
class Subjectinfo(viewsets.ModelViewSet):
    queryset =Subject.objects.all()
    serializer_class=SubjectSerializer
    
class Batchinfo(viewsets.ModelViewSet):
    queryset =Batch.objects.all()
    serializer_class=BatchSerializer
        
class Teacherinfo(viewsets.ModelViewSet):
    queryset =Teacher.objects.all()
    serializer_class=TeacherSerializer

class Studentinfo(viewsets.ModelViewSet):
    queryset =Student.objects.all()
    serializer_class=StudentSerializer
                