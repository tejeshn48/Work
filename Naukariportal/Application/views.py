import logging
import uuid
import django.contrib
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework.authentication import SessionAuthentication
from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import JobSerializer,ApplicantSerializer,ExperienceSerializer,CompanySerializer,QualificationSerializer,SkillSerializer,ReruiterSerializer
from .models import Applicant,Recruiter,Job,Qualification,Skill,Company,Experience,User
# Create your views here.
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
import pandas as pd
from django.conf import settings
# @api_view(["POST"])
# def find_job(request):
#     jobs = Job.objects.filter(title=request.data['title'],city=request.data['city'],skill=request.data['skill'])
#     serializer = Job_serializer(jobs,many=True)
#     return Response(serializer.data)

class CompanyView(ModelViewSet):

    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [AllowAny]
class RecruiterView(ModelViewSet):
    queryset = Recruiter.objects.all()
    serializer_class = ReruiterSerializer
    permission_classes = [AllowAny]
class SkillView(ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [AllowAny]

class JobView(ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [AllowAny]
    def perform_create(self,request):
        posted_by = self.request.user
        JobSerializer.save(posted_by)
        return Response({'status':200})

class Excel(APIView):
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        user = request.user
        print(user)
        jobobj = Job.objects.filter(posted_by=user)
        print(jobobj)
        serializer= JobSerializer(jobobj, many=True)
        df =pd.DataFrame(serializer.data)
        print(df)

        subject="welcome"
        message=df.to_csv(f"static/{uuid.uuid4()}.csv")
        from_email="tejeshn48@gmail.com"
        recipient_list=["tej578@gmail.com","tejeshn48@gmail.com"]
        # to_list ="tejeshn48@gmail.com"
        send_mail(subject,message,from_email,recipient_list)
        return Response({'status':200})

    # , 'fileloc': f"static/{uuid.uuid4()}.csv"
    #


class ApplicationView(ModelViewSet):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer
    permission_classes = [AllowAny]
class ExperinceView(ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    permission_classes = [AllowAny]
class QualificationView(ModelViewSet):
    queryset = Qualification.objects.all()
    serializer_class = QualificationSerializer
    permission_classes = [AllowAny]
