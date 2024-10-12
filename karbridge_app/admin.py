from django.contrib import admin
from .models import KarfarmaProfile, JobPosting, Product, KarjoProfile, Resume, Ticket, OrganizationProfile

# ثبت مدل‌ها در ادمین
admin.site.register(KarfarmaProfile)
admin.site.register(JobPosting)
admin.site.register(Product)
admin.site.register(KarjoProfile)
admin.site.register(Resume)
admin.site.register(Ticket)
admin.site.register(OrganizationProfile)