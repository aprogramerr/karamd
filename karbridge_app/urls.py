from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    KarfarmaProfileViewSet,
    JobPostingViewSet,
    ProductViewSet,
    KarjoProfileViewSet,
    ResumeViewSet,
    TicketViewSet,
    OrganizationProfileViewSet,
)

router = DefaultRouter()
router.register(r'karfarma_profiles', KarfarmaProfileViewSet)
router.register(r'job_postings', JobPostingViewSet)
router.register(r'products', ProductViewSet)
router.register(r'karjoprofiles', KarjoProfileViewSet)
router.register(r'resumes', ResumeViewSet)
router.register(r'tickets', TicketViewSet)
router.register(r'organizationprofiles', OrganizationProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
