from django.urls import path,include
from . import views
from rest_framework import routers

router  = routers.DefaultRouter()
router.register('courses',views.Courseinfo)
router.register('subjects',views.Subjectinfo)
router.register('batches',views.Batchinfo)
router.register('teachers',views.Teacherinfo)
router.register('students',views.Studentinfo)
urlpatterns = [
    path('',include(router.urls))
]