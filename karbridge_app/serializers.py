from rest_framework import serializers
from .models import Karfarma, Organization, JobPosting, Job_skill, Benefits_And_Facilities, Product, Karjo, Resume, Educational_Level, Organization_Name

class KarfarmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Karfarma
        fields = '__all__'

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'

class JobPostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPosting
        fields = '__all__'

class JobSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job_skill
        fields = '__all__'

class BenefitsAndFacilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Benefits_And_Facilities
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class KarjoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Karjo
        fields = '__all__'

class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = '__all__'

class EducationalLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Educational_Level
        fields = '__all__'

class OrganizationNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization_Name
        fields = '__all__'
