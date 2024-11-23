from rest_framework import serializers
from .models import (
    Karfarma,
    Organization,
    JobPosting,
    JobCategory,
    Job_skill,
    Benefits_And_Facilities,
    Product,
    Karjo,
    Resume,
    Job_skill_Resume,
    Educational_Level,
    Organization_Name,
)

class KarfarmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Karfarma
        fields = ['user']  

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = [
            'auther', 'name', 'phone_number', 'email', 'website_address',
            'logo', 'about', 'activity_area', 'state', 'addres_organization',
            'number_of_employees', 'year_of_establishment',
            'profile_background_image', 'media'
        ]

class JobPostingSerializer(serializers.ModelSerializer):
    organization = OrganizationSerializer()  # نمایش اطلاعات سازمان داخل آگهی
    class Meta:
        model = JobPosting
        fields = [
            'organization', 'title', 'category', 'gender', 'employment_type',
            'military_service_status', 'salary', 'state', 'city',
            'minimum_educational_qualification', 'work_history', 'job_skill',
            'benefits_and_facilities', 'posted_date'
        ]

class JobCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = JobCategory
        fields = ['id', 'name']

class JobSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job_skill
        fields = ['name', 'proficiency_level']

class BenefitsAndFacilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Benefits_And_Facilities
        fields = ['name']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['karfarma', 'name', 'description', 'price', 'image', 'created_at', 'updated_at']

class KarjoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Karjo
        fields = ['user']

class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = [
            'karjo', 'date_of_birth', 'marital_status', 'gender',
            'military_status', 'city', 'state', 'address', 'about_me',
            'educational_level', 'organization_name', 'skill', 'instagram_address',
            'linkedin_address', 'github_address', 'resume_attachment'
        ]

class JobSkillResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job_skill_Resume
        fields = ['name', 'proficiency_level']

class EducationalLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Educational_Level
        fields = [
            'educational_level', 'field_of_study', 'university_name',
            'education_start_date', 'education_end_date'
        ]

class OrganizationNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization_Name
        fields = ['organization_name', 'title', 'job_start_date', 'job_end_date']
