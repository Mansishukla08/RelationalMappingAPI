from django.db import models

# Create your models here.
class Subject(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    def __str__(self):
        return self.name+" "+self.description
    class Meta:
        db_table="subject"    

class Course(models.Model):
    name=models.CharField(max_length=100) 
    duration=models.CharField(max_length=100)
    fees=models.IntegerField() 
    subjects=models.ManyToManyField(Subject)
    def __str__(self):
        return self.name
    class Meta:
        db_table="course"

class Batch(models.Model):
    start_time=models.TimeField()
    end_time=models.TimeField()
    start_date=models.DateField()
    courses=models.ForeignKey(Course,on_delete=models.CASCADE,related_name="batches")
    def __str__(self):
        return str(self.start_date)+" "+str(self.start_time)
    class Meta:
        db_table="batch"

class Teacher(models.Model):
    name=models.CharField(max_length=100) 
    address=models.CharField(max_length=100)
    age=models.IntegerField()
    gender=models.CharField(max_length=100) 
    email=models.CharField(max_length=100)
    dob=models.DateField() 
    experience=models.CharField(max_length=100) 
    batches=models.ManyToManyField(Batch)

    def __str__(self):
        return self.name+" "+self.address
    class Meta:
        db_table="teacher"
 
class Student(models.Model):
    name=models.CharField(max_length=100) 
    address=models.CharField(max_length=100)
    age=models.IntegerField()
    gender=models.CharField(max_length=100) 
    email=models.CharField(max_length=100)
    dob=models.DateField()  
    batches=models.ManyToManyField(Batch)
    teachers=models.ManyToManyField(Teacher)
    def __str__(self):
        return self.name
    class Meta:
        db_table="student"