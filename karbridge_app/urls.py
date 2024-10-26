from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import KarfarmaViewSet, OrganizationViewSet, JobPostingViewSet, JobSkillViewSet, BenefitsAndFacilitiesViewSet, ProductViewSet, KarjoViewSet, ResumeViewSet, EducationalLevelViewSet, OrganizationNameViewSet
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path

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

schema_view = get_schema_view(
    openapi.Info(
        title="عنوان API شما",
        default_version="v1",
        description="توضیحات API",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # آدرس Swagger UI
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    # آدرس Redoc UI
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]