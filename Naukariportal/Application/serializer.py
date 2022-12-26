from rest_framework.serializers import ModelSerializer
from .models import Company, Recruiter, Job, Skill, Applicant, Experience, Qualification


class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"


class ReruiterSerializer(ModelSerializer):
    companys = CompanySerializer(read_only=True)

    class Meta:
        model = Recruiter
        fields = "__all__"


class SkillSerializer(ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"


class JobSerializer(ModelSerializer):
    companys = CompanySerializer(read_only=True)
    skill = SkillSerializer(read_only=True)

    class Meta:
        model = Job
        fields = ("title", "description", "max_salary", "min_salary", "employment_type",
                  "max_experience", "min_experience", "city", "company", "location", "industry_type", "skill_type",
                  "companys", "skill")


class ApplicantSerializer(ModelSerializer):
    jobs = JobSerializer(read_only=True)
    recruiter = ReruiterSerializer(read_only=True, many=True)

    class Meta:
        model = Applicant
        fields = ("__all__")


class ExperienceSerializer(ModelSerializer):
    companys = CompanySerializer(read_only=True)
    applicant = ApplicantSerializer(read_only=True, many=True)

    class Meta:
        fields = "__all__"
        model = Experience


class QualificationSerializer(ModelSerializer):
    applicant = ApplicantSerializer(read_only=True)

    class Meta:
        fields = ("__all__")
        model = Qualification
