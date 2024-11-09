from django.contrib import admin
from .models import (
    Karfarma,
    JobPosting,
    Job_skill,
    JobCategory,
    Product,
    Karjo,
    Resume,
    Organization,
    Benefits_And_Facilities,
    Educational_Level,
    Organization_Name,
)

# ثبت مدل‌ها در ادمین
admin.site.register(Karfarma)
admin.site.register(JobPosting)
admin.site.register(Job_skill)
admin.site.register(JobCategory)
admin.site.register(Product)
admin.site.register(Karjo)
admin.site.register(Resume)
admin.site.register(Organization)
admin.site.register(Benefits_And_Facilities)
admin.site.register(Educational_Level)
admin.site.register(Organization_Name)