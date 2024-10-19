from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import KarfarmaViewSet, OrganizationViewSet, JobPostingViewSet, JobSkillViewSet, BenefitsAndFacilitiesViewSet, ProductViewSet, KarjoViewSet, ResumeViewSet, EducationalLevelViewSet, OrganizationNameViewSet

router = DefaultRouter()
router.register(r'karfarma', KarfarmaViewSet)
router.register(r'organization', OrganizationViewSet)
router.register(r'jobposting', JobPostingViewSet)
router.register(r'jobskill', JobSkillViewSet)
router.register(r'benefits', BenefitsAndFacilitiesViewSet)
router.register(r'product', ProductViewSet)
router.register(r'karjo', KarjoViewSet)
router.register(r'resume', ResumeViewSet)
router.register(r'educationallevel', EducationalLevelViewSet)
router.register(r'organizationname', OrganizationNameViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
