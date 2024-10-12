from rest_framework import viewsets
from .models import KarfarmaProfile, JobPosting, Product, KarjoProfile, Resume, Ticket,OrganizationProfile
from .serializers import (
    KarfarmaProfileSerializer,
    JobPostingSerializer,
    ProductSerializer,
    KarjoProfileSerializer,
    ResumeSerializer,
    TicketSerializer,
    OrganizationProfileSerializer,
)

class KarfarmaProfileViewSet(viewsets.ModelViewSet):
    queryset = KarfarmaProfile.objects.all()
    serializer_class = KarfarmaProfileSerializer

class JobPostingViewSet(viewsets.ModelViewSet):
    queryset = JobPosting.objects.all()
    serializer_class = JobPostingSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class KarjoProfileViewSet(viewsets.ModelViewSet):
    queryset = KarjoProfile.objects.all()
    serializer_class = KarjoProfileSerializer

class ResumeViewSet(viewsets.ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class OrganizationProfileViewSet(viewsets.ModelViewSet):
    queryset = OrganizationProfile.objects.all()
    serializer_class = OrganizationProfileSerializer