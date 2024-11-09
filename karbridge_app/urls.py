from django.urls import path
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter
from .views import (
    KarfarmaViewSet,
    OrganizationViewSet,
    JobPostingViewSet,
    JobSkillViewSet,
    BenefitsAndFacilitiesViewSet,
    ProductViewSet,
    KarjoViewSet,
    ResumeViewSet,
    EducationalLevelViewSet,
    OrganizationNameViewSet,
    register_user
)


router = DefaultRouter()
router.register(r'karfarma', KarfarmaViewSet)
router.register(r'organization', OrganizationViewSet)
router.register(r'job-posting', JobPostingViewSet)
router.register(r'jobskill', JobSkillViewSet)
router.register(r'benefits', BenefitsAndFacilitiesViewSet)
router.register(r'product', ProductViewSet)
router.register(r'karjo', KarjoViewSet)
router.register(r'resume', ResumeViewSet)
router.register(r'educationallevel', EducationalLevelViewSet)
router.register(r'organizationname', OrganizationNameViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    # مسیر دریافت توکن
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # مسیر رفرش توکن
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', register_user, name='register_user'),
]
