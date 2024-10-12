from rest_framework import serializers
from .models import KarfarmaProfile, JobPosting, Product, KarjoProfile, Resume, Ticket, OrganizationProfile

class KarfarmaProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = KarfarmaProfile
        fields = '__all__'  # یا می‌توانید فیلدهای خاصی را مشخص کنید

class JobPostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPosting
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class KarjoProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = KarjoProfile
        fields = '__all__'

class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = '__all__'

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'

class OrganizationProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationProfile
        fields = '__all__'