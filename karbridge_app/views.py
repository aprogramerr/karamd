from rest_framework import viewsets
from rest_framework import status , generics, filters
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django_filters.rest_framework import DjangoFilterBackend
from .models import (
    Karfarma,
    Organization,
    JobPosting,
    Job_skill,
    Benefits_And_Facilities,
    Product,
    Karjo,
    Resume,
    Educational_Level,
    Organization_Name
)
from .serializers import (
    KarfarmaSerializer,
    OrganizationSerializer,
    JobPostingSerializer,
    JobSkillSerializer,
    BenefitsAndFacilitiesSerializer,
    ProductSerializer,
    KarjoSerializer,
    ResumeSerializer,
    EducationalLevelSerializer,
    OrganizationNameSerializer
)
from .permissions import IsKarfarma, IsKarjo  

class KarfarmaViewSet(viewsets.ModelViewSet):
    queryset = Karfarma.objects.all()
    serializer_class = KarfarmaSerializer
    permission_classes = [IsKarfarma]  


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [IsKarfarma]  


class JobPostingViewSet(viewsets.ModelViewSet):
    queryset = JobPosting.objects.all()
    serializer_class = JobPostingSerializer
    permission_classes = [IsKarfarma]  


class JobSkillViewSet(viewsets.ModelViewSet):
    queryset = Job_skill.objects.all()
    serializer_class = JobSkillSerializer
    permission_classes = [IsKarfarma]  


class BenefitsAndFacilitiesViewSet(viewsets.ModelViewSet):
    queryset = Benefits_And_Facilities.objects.all()
    serializer_class = BenefitsAndFacilitiesSerializer
    permission_classes = [IsKarfarma]  


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsKarfarma]  


class KarjoViewSet(viewsets.ModelViewSet):
    queryset = Karjo.objects.all()
    serializer_class = KarjoSerializer
    permission_classes = [IsKarjo]  


class ResumeViewSet(viewsets.ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    permission_classes = [IsKarjo]  


class EducationalLevelViewSet(viewsets.ModelViewSet):
    queryset = Educational_Level.objects.all()
    serializer_class = EducationalLevelSerializer
    permission_classes = [IsKarjo]  


class OrganizationNameViewSet(viewsets.ModelViewSet):
    queryset = Organization_Name.objects.all()
    serializer_class = OrganizationNameSerializer
    permission_classes = [IsKarjo]  

######################### TOKEN ##################################
@api_view(['POST'])
def register_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')
    if username and password and email:
        user = User.objects.create_user(username=username, password=password, email=email)
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_201_CREATED)
    return Response({'error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)
