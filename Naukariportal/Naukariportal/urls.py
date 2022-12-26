from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Application.views import *

# Create Router Object
router = DefaultRouter()

# Register View Class with Router


from django.urls import path,include
from Application.views import CompanyView,QualificationView,RecruiterView,ApplicationView,JobView,SkillView,ExperinceView
from rest_framework import routers
router=routers.DefaultRouter()
router.register('Com',CompanyView)
router.register('Job',JobView, basename='Job')
router.register('Re',RecruiterView)
router.register('Sk',SkillView)
router.register('App',ApplicationView)
router.register('Exp',ExperinceView)
router.register('Qe',QualificationView)

urlpatterns =[
    path("",include(router.urls))
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('excel/', Excel.as_view()),
    path("",include(router.urls))
]
